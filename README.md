# lifx-iot-lambda-switch
Ridiculously unnecessary light switch for a LIFX wifi bulb, using an [AWS IoT Button](https://aws.amazon.com/iotbutton/) and [AWS Lambda](https://aws.amazon.com/lambda/)


### Why did I make this?
That's a great question.  I actually made this about two years ago when I thought the hype for serverless architectures had peaked (lol).  I wanted to try out something in the IoT space and get more experience with AWS without having to do something actually difficult.  

### Setup
1. You'll need to purchase an [AWS IoT Button](https://aws.amazon.com/iotbutton/)
2. You'll also need a [LIFX lightbulb](https://www.lifx.com/)
2. Follow the directions on the AWS docs to [configure the button](https://aws.amazon.com/iotbutton/)
3. Follow the instructions to [connect the button to lambda](https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html)
4. Generate an authentication method for the bulb.  You can use OATH, but I just generated an API key [here](
https://cloud.lifx.com/settings) since that's way easier
5. Upload this code to the lambda function from earlier
6. Set a lambda environment variable called "API_KEY" with your API token
6. Ta-da!  You now have a $20 lightswitch that takes 7-10 seconds to work and is dependant on your wi-fi connection (_I never said this was a good idea_)

### Usage
Once you follow the setup process, every time you press the IoT button, it will toggle *all* of your lights.  That's because I used the "all" endpoint since I only had one light anyway.  You can specify groups and more specific IDs as well.  Check out the [API Docs](https://api.developer.lifx.com/docs) if you're interested.

### Extensions
This script only has a single function regardless of how you press the button, but there's actually 3 possible states: SINGLE, DOUBLE, and LONG.  These are received in the "clickType" field of the event.  A possible extension would be to trigger different _scenes_ or colors based on what type of click you used.
