
StudentList = {}
CommandList = {
    'help',
    'add',
    'del',
    'ls'
}
inputText = ""
# 获取学生信息
# StudentId = 学号
# return = 找到返回学生信息，未找到返回False
def getStudentId(StudentId):
    Index = 0
    StudentInfoList = {}
    for ids in StudentList:
        StudentInfo = StudentList.get(ids)
        for sid in StudentId:
            if StudentInfo.get('Student_Id') == sid:
                StudentInfo['Index'] = ids
                StudentInfoList[Index] = StudentInfo
                Index+=1
    else:
        return StudentInfoList

# 添加学生信息
# Id = 学号
# Name = 姓名
# Class = 班级
# Age = 年龄
# return = 返回在学生列表中的索引
def addStudentId(Id, Name, Class, Age):
    if Id and Name and Class and Age:
        StudentList[len(StudentList)] = {"Student_Id": Id, "Student_Name": Name, "Student_Class": Class, "Student_Age": Age}
        print("学号:{} 学生:{} 添加成功! 索引:{}".format(Id, Name, len(StudentList)-1))
        return len(StudentList)
    else:
        return False

# 删除学生信息
# Id = 学号
# 返回True或False
def delStudent(Id):
    Index = getStudentId(Id)
    for Iid in Index:
        del StudentList[Index.get(Iid).get('Index')]
        print("学号:{} 的学生信息已删除 学生信息:{}".format(Index.get(Iid).get('Student_Id'),Index.get(Iid)))
        return True

if __name__ == "__main__":
    print("欢迎访问学生管理系统\n未完成，基本的添加与删除和查询可使用，返回的信息没有进行处理都是字典形式输出\n输入 help 获得帮助")
    while inputText!="exit":
        if inputText!="":
            Command = inputText.split(" ",1)[0]
            ages = inputText.split(" ")
            inputText = ""
            if Command in CommandList:
                # ages索引表示:
                # 1 = 学号 2 = 姓名 3 = 班级 4 = 年龄
                if Command == "add" and len(ages)==5:
                    if not getStudentId({ages[1]}):
                        addStudentId(ages[1],ages[2],ages[3],ages[4])
                    else:
                        print("学号:{} 添加失败! 原因:此学号已存在。".format(ages[1]))
                elif Command == "del":
                    delStudent(ages[1:])
                elif Command == "ls":
                    if len(ages)<2:
                        print(StudentList)
                    else:
                        print(getStudentId(ages[1:]))
                elif Command == "help":
                    print("""
                    add <学号> <姓名> <班级> <年龄>
                    del <学号>
                    ls [学号...] 多个查询，空格分隔 不填学号则列出所有信息
                    """)
                else:
                    print("未知命令,可能格式出现问题，请输入 help 获得帮助")
            else:
                print(Command+" 是个未知指令")
        else:
            inputText = input(">>>")
    else:
        print("退出...")
