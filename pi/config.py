# CHANGE THIS FILE TO REFLECT YOUR SETUP

### Constants
LIGHT_OFF = 0
LIGHT_ON = 1
LIGHT_BLINKING = 2

WASHER = 100
DRYER = 101

PAY_EZLINK = 200
PAY_COIN = 201

# Number of seconds to count on/off cycles for to check for blinking
ON_OFF_COUNT_INTERVAL_SEC = 6
ON_OFF_COUNT_BLINK_THRESHOLD = 2

# Which pin will be used to control the test LED (during debugging)
#TEST_GPIO_PIN = 18
#LED_PIN = 12

# Debouncing time
BOUNCETIME = 50

# Floor number for installed pi
FLOOR_NUMBER = "9"

MACHINES = [
        {	"pin":17, "name":"WASHER A (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":22, "name":"WASHER B (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":10, "name":"WASHER C (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":5, "name":"WASHER D (COIN)", "machinetype": WASHER, "paymenttype":PAY_COIN	},
	{	"pin":26,  "name":"WASHER E (COIN)", "machinetype": WASHER, "paymenttype":PAY_COIN	},
]

# Unique device ID so each floor can have multiple Raspberry Pis collecting data and not overwrite other pi's data on Firebase
PI_DEVICE_ID = None