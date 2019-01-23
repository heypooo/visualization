import file_set
import graph


print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□     Data Visualization       □□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□         A B O U T            □□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□    Occupational disease      □□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")

print("\n                                                                            Test Program")

#파일 로드 후 셋팅
file_name = input("\n\n파일 이름을 입력하세요: ")

df_file = file_set.File_set()
data = df_file.file_load(file_name)

# 데이터프레임 리스트 셋팅
df_file.data_columns(data) #컬럼 리스트 생성
df_file.data_classification(data) # 범주/이산형 데이터 분류
df_file.list_mining(data) #새로운 컬럼 리스트 생성
df_file.newData_classification(data) # 새로운 범주/이산형 데이터 분류
columns = df_file.get_newColumns()
letter = df_file.get_newLetter()
number = df_file.get_newNumber()
df_file.set_except(letter,number)

df_graph = graph.Graph()

print("\n\n□□□□□□□□□□□□        File loading completed         □□□□□□□□□□□□")
print(" Graph Number ")


while(True):
    graph_number = int(
        input("\n\n1. bar\n2. bar2 \n3. box plot\n4. scatter plot\n5. histogram\n6. 3D projection\n7. 정규화 검사\n8. 종료\n\n\nPlease select a number:"))

    if graph_number == 1:
        var = input("\n변수를 입력하세요: ")
        df_graph.bar(data,var)

    elif graph_number == 2:
        var = input("\n변수를 입력하세요: ")
        df_graph.bar2(data, var)

    elif graph_number == 3:
        var1 = input("\n첫 번째 변수를 입력하세요: ")
        var2 = input("\n두 번째 변수를 입력하세요: ")
        df_graph.box_plot(data,var1,var2)

    elif graph_number == 4:
        var1 = input("\n첫 번째 변수를 입력하세요: ")
        var2 = input("\n두 번째 변수를 입력하세요: ")
        df_graph.scatter_plot(data, var1, var2)

    elif graph_number == 5:
        var1 = input("\n첫 번째 변수를 입력하세요: ")
        var2 = input("\n두 번째 변수를 입력하세요: ")
        df_graph.histogram(data, var1, var2)

    elif graph_number == 6:
        var1 = input("\n첫 번째 변수를 입력하세요: ")
        var2 = input("\n두 번째 변수를 입력하세요: ")
        df_graph.projection(data, var1, var2)

    elif graph_number == 7:
        var = input("\n변수를 입력하세요: ")
        df_graph.normal_check(data,var)

    elif graph_number == 8:
        print("\n프로그램을 종료합니다.")
        break







