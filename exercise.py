student_name=input("Enter your name: ")
course_work_mark=int(input("Enter your course work mark: "))
exam_score=int(input("Enter your exam mark: "))

compute_exam_mark=(exam_score /100 )* 70
compute_final_score=(compute_exam_mark + course_work_mark)

print(f"your exam mark is {compute_exam_mark}\n your final mark is {compute_final_score}")
