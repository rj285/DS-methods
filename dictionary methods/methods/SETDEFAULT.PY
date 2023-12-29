#setdefault method in dict

student_scores = { 'alice':85, 'bob':90, 'charlie':78 }


alice_score = student_scores.setdefault('alice',0)
print(f"Alice score: {alice_score}")
print(student_scores)

#new key pair value stores in dict last end
david_score = student_scores.setdefault('david',0)
print(f"david score: {david_score}")
print(student_scores)