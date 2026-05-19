# ==========================================================
# MATRIX OPERATIONS AND REAL-WORLD APPLICATIONS
# STREAMLIT PROJECT
# ==========================================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Matrix Operations Project",
    page_icon="📘",
    layout="wide"
)

st.title("📘 Matrix Operations and Real-World Applications")

st.write("""
This project explains matrix operations using simple and interactive examples.

Topics Included:
- Matrix Addition
- Matrix Multiplication
- Matrix Transpose
- Matrix Inverse
- Associativity Proof
- Non-Commutativity Proof
- Population Prediction Model
- Economic Input-Output Model
""")


# ==========================================================
# SIDEBAR MENU
# ==========================================================

menu = st.sidebar.selectbox(
    "Choose Topic",
    [
        "Addition",
        "Multiplication",
        "Transpose",
        "Inverse",
        "Associativity Proof",
        "Non-Commutativity Proof",
        "Population Prediction",
        "Economic Model"
    ]
)


# ==========================================================
# MATRIX INPUT FUNCTION
# ==========================================================

def matrix_input(name):

    st.subheader(f"Enter Matrix {name}")

    rows = st.number_input(
        f"Rows of Matrix {name}",
        min_value=1,
        max_value=5,
        value=2
    )

    cols = st.number_input(
        f"Columns of Matrix {name}",
        min_value=1,
        max_value=5,
        value=2
    )

    matrix = []

    for i in range(rows):

        row = st.text_input(
            f"Enter Row {i+1} of Matrix {name} (space separated)",
            key=f"{name}{i}"
        )

        if row:
            matrix.append(list(map(float, row.split())))

    if len(matrix) == rows:

        try:
            return np.array(matrix)

        except:
            st.error("Invalid Matrix Input")

    return None


# ==========================================================
# ADDITION
# ==========================================================

if menu == "Addition":

    st.header("➕ Matrix Addition")

    st.write("""
    Matrix addition means adding corresponding elements.

    Example:
    """)

    st.latex(r"A + B")

    A = matrix_input("A")
    B = matrix_input("B")

    if st.button("Perform Addition"):

        try:

            result = A + B

            st.success("Addition Performed Successfully")

            st.write("Matrix A")
            st.write(A)

            st.write("Matrix B")
            st.write(B)

            st.write("Result")
            st.write(result)

        except:
            st.error("Matrices must have same dimensions")


# ==========================================================
# MULTIPLICATION
# ==========================================================

elif menu == "Multiplication":

    st.header("✖️ Matrix Multiplication")

    st.write("""
    Matrix multiplication is performed using rows and columns.
    """)

    st.latex(r"AB")

    A = matrix_input("A")
    B = matrix_input("B")

    if st.button("Perform Multiplication"):

        try:

            result = np.dot(A, B)

            st.success("Multiplication Successful")

            st.write("Result")
            st.write(result)

        except:
            st.error("Invalid dimensions for multiplication")


# ==========================================================
# TRANSPOSE
# ==========================================================

elif menu == "Transpose":

    st.header("🔄 Matrix Transpose")

    st.write("""
    Transpose changes rows into columns.
    """)

    st.latex(r"A^T")

    A = matrix_input("A")

    if st.button("Find Transpose"):

        result = A.T

        st.success("Transpose Found")

        st.write("Original Matrix")
        st.write(A)

        st.write("Transpose")
        st.write(result)


# ==========================================================
# INVERSE
# ==========================================================

elif menu == "Inverse":

    st.header("🧮 Matrix Inverse")

    st.write("""
    Inverse exists only for square matrices.
    """)

    st.latex(r"A^{-1}")

    A = matrix_input("A")

    if st.button("Find Inverse"):

        try:

            determinant = np.linalg.det(A)

            if determinant != 0:

                result = np.linalg.inv(A)

                st.success("Inverse Found")

                st.write(result)

            else:

                st.error("Inverse not possible")

        except:

            st.error("Enter a square matrix")


# ==========================================================
# ASSOCIATIVITY PROOF
# ==========================================================

elif menu == "Associativity Proof":

    st.header("📐 Associativity Property")

    st.write("""
    Matrix multiplication follows associativity property.
    """)

    st.latex(r"(AB)C = A(BC)")

    A = matrix_input("A")
    B = matrix_input("B")
    C = matrix_input("C")

    if st.button("Verify Associativity"):

        try:

            left = np.dot(np.dot(A, B), C)

            right = np.dot(A, np.dot(B, C))

            st.write("Left Side (AB)C")
            st.write(left)

            st.write("Right Side A(BC)")
            st.write(right)

            if np.array_equal(left, right):

                st.success("Property Verified")

            else:

                st.error("Property Not Verified")

        except:

            st.error("Invalid matrices")


# ==========================================================
# NON-COMMUTATIVITY PROOF
# ==========================================================

elif menu == "Non-Commutativity Proof":

    st.header("📏 Non-Commutativity Property")

    st.write("""
    Matrix multiplication is NOT commutative.
    """)

    st.latex(r"AB \neq BA")

    A = matrix_input("A")
    B = matrix_input("B")

    if st.button("Verify Non-Commutativity"):

        try:

            AB = np.dot(A, B)

            BA = np.dot(B, A)

            st.write("AB")
            st.write(AB)

            st.write("BA")
            st.write(BA)

            if np.array_equal(AB, BA):

                st.success("AB = BA")

            else:

                st.warning("AB ≠ BA")

        except:

            st.error("Invalid matrices")


# ==========================================================
# POPULATION PREDICTION MODEL
# ==========================================================

elif menu == "Population Prediction":

    st.header("🌍 Population Prediction Model")

    st.write("""
    This real-world application uses matrices to predict population growth.
    """)

    st.latex(r"P_{n+1} = AP_n")

    years = st.slider("Select Number of Years", 1, 20, 10)

    transition_matrix = np.array([
        [0.8, 0.1],
        [0.2, 0.9]
    ])

    population = np.array([
        [1000],
        [500]
    ])

    results = []

    for i in range(years):

        population = np.dot(transition_matrix, population)

        results.append(population.flatten())

    df = pd.DataFrame(results, columns=["City A", "City B"])

    st.write("Population Data")
    st.dataframe(df)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(df["City A"], label="City A")
    ax.plot(df["City B"], label="City B")

    ax.set_title("Population Prediction")
    ax.set_xlabel("Years")
    ax.set_ylabel("Population")

    ax.legend()

    st.pyplot(fig)

# ==========================================================
# ECONOMIC INPUT-OUTPUT MODEL
# ==========================================================

elif menu == "Economic Model":

    st.header("💰 Economic Input-Output Model")

    st.write("""
    This real-world application uses matrices in economics.

    Users can manually enter:
    - Industry Consumption Matrix
    - Market Demand Matrix
    """)

    st.latex(r"X = (I - A)^{-1}D")

    # ==================================================
    # MATRIX SIZE
    # ==================================================

    size = st.number_input(
        "Enter Number of Industries",
        min_value=2,
        max_value=5,
        value=2
    )

    st.subheader("Enter Industry Consumption Matrix (A)")

    A = []

    for i in range(size):

        row = st.text_input(
            f"Enter Row {i+1} for Matrix A",
            key=f"A_{i}"
        )

        if row:

            A.append(list(map(float, row.split())))

    st.subheader("Enter Market Demand Matrix (D)")

    D = []

    for i in range(size):

        value = st.text_input(
            f"Enter Demand Value for Industry {i+1}",
            key=f"D_{i}"
        )

        if value:

            D.append([float(value)])

    # ==================================================
    # CALCULATION
    # ==================================================

    if st.button("Calculate Economic Output"):

        try:

            A = np.array(A)

            D = np.array(D)

            # Identity Matrix
            I = np.identity(size)

            # Economic Output
            X = np.dot(np.linalg.inv(I - A), D)

            st.success("Economic Output Calculated Successfully")

            st.subheader("Production Output Matrix")

            output_df = pd.DataFrame(
                X,
                columns=["Production Required"]
            )

            st.dataframe(output_df)

            # ==================================================
            # BAR GRAPH
            # ==================================================

            industries = []

            for i in range(size):

                industries.append(f"Industry {i+1}")

            values = X.flatten()

            fig, ax = plt.subplots(figsize=(8,5))

            ax.bar(industries, values)

            ax.set_title("Economic Production Output")

            ax.set_xlabel("Industries")

            ax.set_ylabel("Production Required")

            st.pyplot(fig)

            # ==================================================
            # LINE GRAPH
            # ==================================================

            fig2, ax2 = plt.subplots(figsize=(8,5))

            ax2.plot(industries, values, marker='o')

            ax2.set_title("Economic Output Trend")

            ax2.set_xlabel("Industries")

            ax2.set_ylabel("Production")

            st.pyplot(fig2)

        except:

            st.error("Please enter valid matrix values")