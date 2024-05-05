import Lab2

print("Test_Lab2")

def test_find_min_max():
    
    input_list = [1,2,3,4,5]
    test_min = 1
    test_max = 5
    result = Lab2.calc_min_max_temperature(input_list)
    assert (result == (test_min, test_max))

def test_calc_average():

    input_list =[1,2,3,4,5]
    test_avg = 3
    result = Lab2.calc_average_temperature(input_list)
    assert (result == (test_avg))

def test_calc_median_temperature():
    
    input_list = [5,2,4,3,1]
    test_med =3 
    result = Lab2.calc_median_temperature(input_list)
    assert  (result ==(test_med))