import time, sys
import requests

from fhict_cb_01.custom_telemetrix import CustomTelemetrix

BUTTON1 = 8
DHTPIN = 12
REDLED = 4
GREENLED = 5
BUZZER = 3
SERVER_END_ORDER_URL = "http://127.0.0.1:5000/notify"
SERVER_START_ORDER_URL = "http://127.0.0.1:5000/start-cooking-order"
SERVER_UPDATE_TEMPTIME_URL = "http://127.0.0.1:5000/oven-status"

level = 0
temp = 0
oven_orders = []
elapsed_times = []
order = 1
no_orders_message_printed = False

initial_timer = 60
current_timer = initial_timer

def Measure(data):
    global temp
    if (data[1] == 0):
        temp = data[5]

def ButtonChanged(data):
    global level, order, oven_orders, elapsed_times, current_timer
    level = data[2]

    if level == 0:
        print("Button was pressed!")
        send_pizza_started_notification()
        oven_orders.append(time.time())
        elapsed_times.append(0)
        current_timer = initial_timer

def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_digital_input_pullup(BUTTON1, callback=ButtonChanged)
    board.displayOn()
    board.set_pin_mode_dht(DHTPIN, dht_type=11, callback=Measure)
    board.set_pin_mode_digital_output(REDLED)
    board.set_pin_mode_digital_output(GREENLED)
    board.set_pin_mode_analog_output(BUZZER)

def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{str(minutes).rjust(2, '0')}.{str(seconds).rjust(2, '0')}"

def send_temp_and_time():
    try:
        data = {"temperature": temp+200, "timer": time_str}
        response = requests.post(SERVER_UPDATE_TEMPTIME_URL, json=data)
        if response.status_code == 200:
            print(temp + 200, time_str)
    except Exception as e:
        print(f"Error: {e}")
        

def send_pizza_started_notification():
    try:
        response = requests.post(SERVER_START_ORDER_URL, json={})
        if response.status_code == 200:
            print(f"Started cooking an order")
        else:
            print(f"Failed to start cooking order.")
    except Exception as e:
        print(f"Error: {e}")

def send_pizza_ready_notification(order_number):
    try:
        data = {"order_number": order_number}
        response = requests.post(SERVER_END_ORDER_URL, json=data)
        if response.status_code == 200:
            print(f"Pizza Order #{order_number} is ready and notification sent successfully!")
            control_buzzer()
        else:
            print(f"Failed to send pizza ready notification for Order #{order_number}.")
    except Exception as e:
        print(f"Error: {e}")

def control_buzzer():
    board.analog_write(BUZZER, 127)
    time.sleep(1)
    board.analog_write(BUZZER, 0)


def loop():
    global temp, time_str, oven_orders, elapsed_times, order, no_orders_message_printed
    while True:
        if not oven_orders:
            if not no_orders_message_printed:
                print("No active orders in the oven.")
                no_orders_message_printed = True
            board.displayShow("done")
            board.digital_write(GREENLED, 1)
        else:
            no_orders_message_printed = False
            for i, order_time in enumerate(oven_orders):
                elapsed_time = time.time() - order_time
                remaining_time = 60 - elapsed_time

                if remaining_time <= 0:
                    send_pizza_ready_notification(order)
                    order += 1
                    oven_orders.pop(i)
                    elapsed_times.pop(i)
                else:
                    elapsed_times[i] = elapsed_time

            board.digital_write(REDLED, 1 if oven_orders else 0)
            board.digital_write(GREENLED, 0 if oven_orders else 1)

            if oven_orders:
                cronometer = max(0, 60 - elapsed_times[0])
                time_str = format_time(cronometer)
                send_temp_and_time()
                board.displayShow(time_str)
            else:
                board.displayShow("1.00")

        time.sleep(1)

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()
        sys.exit(0)







