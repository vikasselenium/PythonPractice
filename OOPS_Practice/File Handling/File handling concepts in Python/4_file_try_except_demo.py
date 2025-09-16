try:
    # Try to open and read a file
    with open("writelines_example.txt", "r") as f:
        content = f.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# finally:
#     f.close()
#     print(f.closed)
# here we haven't used f.close() in finally bock as we used with statement


