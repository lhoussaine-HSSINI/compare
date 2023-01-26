import  os
import  streamlit as st
import  pandas as pd
from urllib.request import urlopen


def main():
    st.title("product cotepara VS product parasconti")
    st.subheader("Bonjour salim")
    list_faylat=["https://res.cloudinary.com/faho-world/raw/upload/v1674691232/media/dataset/cotepara_cx6jc4.csv",
                 "https://res.cloudinary.com/faho-world/raw/upload/v1674691223/media/dataset/parasconti_ejoall.csv"]
    def  file_selector(folder_path="dataset"):
        filenames=["cotepara.csv","parasconti.csv"]
        selected_filename=st.selectbox("product cotepara or parasconti", filenames)
        return  selected_filename

    filename= file_selector()
    st.info("you selected :::  {}".format(filename))
    if filename =="cotepara.csv":
        df=pd.read_csv(list_faylat[0], index_col = [0])
    else:
        data_location = "https://res.cloudinary.com/faho-world/raw/upload/v1674691223/media/dataset/parasconti_ejoall.csv"
        df=pd.read_csv(data_location ,sep="\t", index_col = [0])
    #   show  data
    if st.checkbox("show data"):
        number = st.number_input("Number of rows to view",1)
        st.dataframe(df.head(int(number)))

    #   show  columns
    if st.button("column Names"):
        st.write(df.columns)

    #   show  shep
    if st.checkbox("Shape of Data"):

        data_dim=st.radio("show Dimension By ", ("Rows", "Columns"))
        if data_dim=="Rows":
            st.text("Number of Rows : {}".format(df.shape[0]))
            # st.write(df.shape[0])
        elif data_dim=="Columns":
            st.text("Number of Columns : {}".format(df.shape[1]))
            # st.write(df.shape[1])
        else:
            st.write(df.shape)

    #   select columns
    if st.checkbox("select columns to show"):
        all_columns = df.columns.tolist()
        selected_columns=st.multiselect("select", all_columns)
        if selected_columns:
            new_df = df[selected_columns]
            st.dataframe(new_df)

    #   show data type
    if st.button("Data Types"):
        st.write(df.dtypes)

    #   show summary
    if st.button("Summary"):
        st.write(df.describe().T)


if __name__ == "__main__":
    main()