# Student Hub - Sambhal
# Made by Nidhi Chaudhary
# Python + Pandas + NumPy + Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------
# PG DATA
# ---------------------------
pg_data = {
    "Room Type": ["Single Room", "Double Sharing", "Triple Sharing"],
    "Price": [4500, 3000, 2200],
    "Available": [2, 3, 1]
}

df_pg = pd.DataFrame(pg_data)


def show_pg_details():
    print("\n--- PG ROOMS PRICE LIST ---")
    print(df_pg)

    print(f"\nAverage PG Price: Rs. {np.mean(df_pg['Price']):.2f}")
    print(f"Total Rooms Available: {np.sum(df_pg['Available'])}")
    print(f"Highest Price: Rs. {np.max(df_pg['Price'])}")
    print(f"Lowest Price: Rs. {np.min(df_pg['Price'])}")


def exam_preparation():
    print("\n--- EXAM PREPARATION ---")
    print("BCA Notes - Python, DBMS, Maths")
    print("Important Questions - Last 5 Year Papers")
    print("Mock Test - Online Test Series")
    print("Practical File - Ready-made File")


def add_student_request():
    name = input("Enter Your Full Name: ").strip()
    phone = input("Enter 10 Digit Phone Number: ").strip()
    need = input("What do you need? (PG Room / Notes / Exam / Assignment): ").strip()
    message = input("Write Your Details: ").strip()

    if len(phone) != 10 or not phone.isdigit():
        print("Invalid Phone Number!")
        return

    new_data = pd.DataFrame(
        [[name, phone, need, message]],
        columns=["Name", "Phone", "Need", "Message"]
    )

    if os.path.exists("students.csv"):
        old_data = pd.read_csv("students.csv")
        final_data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        final_data = new_data

    final_data.to_csv("students.csv", index=False)

    print("✅ Request Saved Successfully!")


def show_requests():
    if not os.path.exists("students.csv"):
        print("No requests found!")
        return

    df = pd.read_csv("students.csv")

    print("\n--- ALL STUDENT REQUESTS ---")
    print(df)

    print(f"\nTotal Requests: {len(df)}")

    print("\n--- NEED WISE ANALYSIS ---")
    print(df["Need"].value_counts())


def show_graph():
    plt.figure(figsize=(8, 5))

    plt.bar(
        df_pg["Room Type"],
        df_pg["Price"],
        color=["red", "green", "blue"]
    )

    plt.title("PG Rooms Price Comparison - Student Hub Sambhal")
    plt.xlabel("Room Type")
    plt.ylabel("Price (Rs.)")

    plt.tight_layout()
    plt.show()


# ---------------------------
# MAIN PROGRAM
# ---------------------------
print("=" * 40)
print("        STUDENT HUB - SAMBHAL")
print("      Python | NumPy | Pandas")
print("=" * 40)

show_pg_details()

while True:

    print("\n--- MENU ---")
    print("1. Exam Preparation Details")
    print("2. Add New Student Request")
    print("3. Show All Requests + Analysis")
    print("4. Show Graph - PG Price Bar Chart")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        exam_preparation()

    elif choice == "2":
        add_student_request()

    elif choice == "3":
        show_requests()

    elif choice == "4":
        show_graph()

    elif choice == "5":
        print("Thank You! Made by Nidhi Chaudhary")
        break

    else:
        print("Invalid Choice! Please try again.")