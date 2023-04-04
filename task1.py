import pandas as pd
from flask import Flask, request, render_template, send_file


def unique(school_list,unique_school_list):
    for x in school_list:
        if x not in unique_school_list:
            unique_school_list.append(x)
school_list = []
school_name = []
class_number = []
unique_school_list = []
unique_class_list = []
output = []
for_csv = []
df = []
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload():
    global df,school_list,unique_school_list,class_number,unique_class_list,for_csv
    school_name_selected = request.form.get('school')
    class_number_selected = request.form.get('classes')
    for i in range(0,len(df)):
            if school_name_selected == df.iloc[i,2] == school_name_selected:
                if class_number_selected == str(df.iloc[i,1]):    
                    output.append(df.iloc[i,0])
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        for i in range(0,len(df)):
            school_list.append(df.iloc[i,2])
        for i in range(0,len(df)):
            class_number.append(df.iloc[i,1])
        school_list.sort()
        class_number.sort()
        unique(school_list,unique_school_list)
        unique(class_number,unique_class_list)
        school_name_selected = request.form.get('school')
        class_number_selected = request.form.get('classes')
        for i in range(0,len(df)):
            if school_name_selected == df.iloc[i,2] == school_name_selected:
                if class_number_selected == str(df.iloc[i,1]):    
                    output.append(df.iloc[i,0])
                    for_csv.append(df.iloc[i])
        return render_template('index.html',unischools = unique_school_list, classlists = unique_class_list)
    return render_template('index.html',unischools = unique_school_list, classlists = unique_class_list)

@app.route("/dropdown" , methods=['GET', 'POST'])
def dropdown():
    global unique_class_list,unique_school_list
    return render_template('dropdown.html', unischools = unique_school_list, classlists = unique_class_list)

@app.route("/table" , methods=['GET', 'POST'])
def table():
    global df_final
    school_name_selected = request.form.get('school')
    class_number_selected = request.form.get('classes')
    output = []
    for i in range(0,len(df)):
        if school_name_selected == df.iloc[i,2]:
            if class_number_selected == str(df.iloc[i,1]):    
                output.append(df.iloc[i,0])
                for_csv.append([df.iloc[i,0],df.iloc[i,1],df.iloc[i,2]])
    df_final = pd.DataFrame(for_csv, columns = ['Student Id', 'Class', 'School'])
    return render_template('table.html', stu_details = output , school_name = school_name_selected , class_number = class_number_selected)

@app.route('/download')
def download_file():
    global for_csv
    print(for_csv)
    df_final = pd.DataFrame(for_csv, columns = ['Student Id', 'Class', 'School'])
    df_final.to_csv('output.csv')
    path = "D:\BHANU\Python\Internship\Task_1\output.csv"
	#path = "sample.txt"
    return send_file(path, as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True)

