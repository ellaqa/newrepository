import subprocess #to use subprocess
process = subprocess.run(
                        args= ['python3','triangle_two.py','3','3','3'],
                        universal_newlines=True,
                        stdout=subprocess.PIPE
                        )
process_out = process.stdout.splitlines()
print(process_out)
assert process_out == ['The triangle is equilateral ']