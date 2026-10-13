def master_controller(hour, cpu_load):
    # 1. Decide the Mode based on time
    mode = "Low-power Standby"
    if 8 <= hour < 17:
        mode = "Business Mode"
    elif 17 <= hour < 20:
        mode = "Batch Mode"
    elif 20 <= hour <= 23:
        mode = "Hosting Mode"
    elif 0 <= hour < 8:
        mode = "Analytics Mode"

    # 2. Decide the Power State based on server load
    power_state = "Active"
    active_servers = 2  # The bank always keeps 2 servers on for ATMs
    
    if mode == "Business Mode" and cpu_load > 70:
        active_servers = 20
        power_state = "WAKING UP all servers for high daytime traffic!"
    elif mode == "Analytics Mode" and cpu_load < 20:
        active_servers = 5
        power_state = "SAVING POWER: Hibernating 15 servers."

    # 3. Print the final dashboard report
    print(f"--- Data Center Status Report ---")
    print(f"Time: {hour}:00 | Server Load: {cpu_load}%")
    print(f"Current Mode: {mode}")
    print(f"Power Action: {power_state}")
    print(f"Servers Online: {active_servers} / 20")
    print("-" * 35 + "\n")

# Run two simulations to prove it works
print("SIMULATION 1: Busy Tuesday Morning")
master_controller(10, 85) # 10:00 AM, 85% load

print("SIMULATION 2: Quiet Sunday Night")
master_controller(3, 15)  # 3:00 AM, 15% load
