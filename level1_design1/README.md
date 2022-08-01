# Final report: Sudhanshu Singh(level1_design1)
The value assign to the input using


![image](https://user-images.githubusercontent.com/73732594/182029571-5ac35f83-0018-4c3e-8428-89b76283c922.png)

The assertion error seen for one set of random input

![image](https://user-images.githubusercontent.com/73732594/182029702-c8dbe0e3-4abc-4ed2-aaef-65473d3cfa15.png)

# Test Scenerio
*Random Test input for one set: Model= 10 (for selection line 12)

*Expected output for the same set: 10 (for selection line 12)

*Observed output in dut.out.value= 00  (for selection line 12)

 Output mismatched with expected output proving there is a design bug

![image](https://user-images.githubusercontent.com/73732594/182030023-4df5be1d-bd32-44aa-b649-1c4d7394114e.png)

# Design Bug
 Based on above test input and analysing the design we see following

![image](https://user-images.githubusercontent.com/73732594/182030468-80aee04b-059b-49ca-ac1e-98a32f2bb297.png)

For the design, at the place of 5'b01101: out = inp12, it should be 5'b01100: out = inp12

# Design Fix

Updating the design and rerunning the test the test pass

![image](https://user-images.githubusercontent.com/73732594/182030715-97feee16-f489-4ac2-9d2f-1162e4663ac1.png)



