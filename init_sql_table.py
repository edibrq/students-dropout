import kagglehub
import pandas as pd
from sqlalchemy import create_engine

DATASET_NAME = "students_dropout_academic_success.csv"
DATABASE_URI = "postgresql://localhost:5432/students_db"


def to_snake_case(s):
    return s.lower().replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').strip()


def convert_column_names(df):
    df.columns = [to_snake_case(col) for col in df.columns]


def create_database(df):
    engine = create_engine(DATABASE_URI)
    table_name = 'student_academic_success'

    # Write DataFrame to SQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def main():
    path = kagglehub.dataset_download("adilshamim8/predict-students-dropout-and-academic-success")
    dataset_path = f"{path}/{DATASET_NAME}"
    print("Path to dataset files:", dataset_path)

    df = pd.read_csv(dataset_path)
    convert_column_names(df)

    print("Converted column names:")
    print(list(df.columns.values))
    
    create_database(df)


if __name__ == '__main__':
    main()

