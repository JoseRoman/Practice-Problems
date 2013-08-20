def student_manager(students):
    number_count =  0
    class_total = 0

    for i in range (len(students)):
        print (students[i][0],'Student average =', sum(students[i][1:])/len(students[i][1:]))
        for number in students[i][1:]:
            number_count+=1
            class_total+=number
    print ('Class average =', class_total/number_count)
