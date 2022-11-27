
local SUBSET_SIZE = os.getenv("SUBSET_SIZE") or 0
local SUBSET_RUN_TIME = os.getenv("SUBSET_RUN_TIME") or 0

function indexOf(array, value)
    for i, v in ipairs(array) do
        if v == value then
            return i
        end
    end
    return nil
end

function dump(array, offset)
    for i, v in ipairs(array) do
        if type(v) == "table" then
            offset = offset .. "   "
            dump(v, offset)
        else
            print(offset, i, " = ", v)
        end
    end
end

-- read number or ip addresses available 
local total = 0
function readIpCount()
    if total == 0 then
        local handle = io.popen("kubectl get services | grep sb- | wc -l")
        total = handle:read("*a")
        handle:close()
    end
    return total
end

function readRandomSeed()
    -- init random seed
    local inp = io.open("/dev/random", "rb")
    local data = inp:read(4)
    inp:close()
    local s = string.byte(data, 1, string.len(data))
    local n = tonumber(s)
    return n
end

function get_subset(max)
    local subset = {}
    for i = 1,SUBSET_SIZE do
        local idx = math.random(max)
        subset[i] =  "/" .. idx .. "/greeting"
    end
    return subset
end

local counter = 1
local threads = {}

function setup(thread)
    thread:set("id", counter)
    thread:set("subset_start", 0)  
    thread:set("current_subset", nil)
    thread:set("report", "")
    local max = readIpCount()
    thread:set("random_max", max)
    table.insert(threads, thread)
    counter = counter + 1
end

function init(args)
    local seed = readRandomSeed()
    math.randomseed(seed)
end

function request()
    if subset_start + SUBSET_RUN_TIME < os.time()  then 
        report = report .. "New subset\n" 
        current_subset = get_subset(random_max)
        subset_start = os.time()
    end
    local t = os.clock()
    print("clock=", tostring(t))
    local ms = string.match(tostring(t), "%d%.(%d+)")
    print("ms=", ms)
    local path = current_subset[math.random(SUBSET_SIZE)]
    
    report = report .. path .. "\t" .. os.date('%H:%M:%S', os.time()) .. ms .. "\n"

    return wrk.format("GET", path)
end


function done(summary, latency, requests)
    print("---------- Custom Report -------------")
    for index, thread in ipairs(threads) do
        local id        = thread:get("id")
        local report    = thread:get("report")
        print("Thread ", id)
        print(report)
    end    
end