# Final report: Sudhanshu Singh(level1_design1)
The value assign to the input using:
For Bug 1

![image](https://user-images.githubusercontent.com/73732594/182031550-5bbf9291-eda2-4e80-adb1-eccb1cb241a7.png)

For Bug 2

![image](https://user-images.githubusercontent.com/73732594/182031582-8c8361fb-f05c-4a0c-9a25-0de96e7f81db.png)


The assertion error seen 
For Bug 1

![image](https://user-images.githubusercontent.com/73732594/182031773-2e18f68c-883c-4bd7-ab2a-5dab8f6de63b.png)

For Bug 2

![image](https://user-images.githubusercontent.com/73732594/182031805-d0f8866d-4315-49e4-a303-5cad868cac58.png)


# Test Scenerio
For Bug1

* For Current state 001, given inp_bit=1
* Expected  current state  : 001
* Observed output in dut.current_state.value= 000

For Bug 2
* For Current state 101, given inp_bit=1
* Expected  current state  : 010
* Observed output in dut.current_state.value= 000

 Output mismatched with expected output proving there is a design bug


# Design Bug
 Based on above test input and analysing the design we see following
For Bug 1

![image](https://user-images.githubusercontent.com/73732594/182032461-bb0d5633-c64e-4fbc-8a08-6093b1f0b665.png)


For the design, at the place of  'next_state = IDLE' it should be  'next_state = SEQ_1'

For Bug2

![image](https://user-images.githubusercontent.com/73732594/182032391-f45a6970-46ba-440f-a53d-7db92e3460bc.png)

For the design, at the place of  'next_state = IDLE' it should be  'next_state = SEQ_10

# Design Fix

Updating the design and rerunning the test the test pass





![image](https://user-images.githubusercontent.com/73732594/182032795-4c6c6136-4fff-4013-b3d5-2bcee2b2b64b.png)


