import Task0 as t;



def tests():

    assert t.text_first_record[0] == '97424 22395';
    assert t.text_first_record[1] == '90365 06212';
    assert t.text_first_record[2] == '01-09-2016 06:03:22';


    assert t.call_last_record[0] == '98447 62998';
    assert t.call_last_record[1] == '(080)46304537';
    assert t.call_last_record[2] == '30-09-2016 23:57:15';
    assert t.call_last_record[3] == '2151';



    print('All tests passed')


tests();
