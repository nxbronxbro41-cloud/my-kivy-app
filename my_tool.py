import datetime

name = input("अपना नाम दर्ज करें: ")
current_time = datetime.datetime.now().strftime("%I:%M %p")

print(f"\nनमस्ते {name}! आपके टूल में आपका स्वागत है।")
print(f"अभी समय हो रहा है: {current_time}")

