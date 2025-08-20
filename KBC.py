questions = [
  [
      "Which is a JavaScript data type?", "Float", "Number", "Character",
      "Decimal", 2
  ],
  [
      "What does the 'id' attribute in HTML do?", "Applies class style",
      "Creates a link", "Assigns a unique identifier", "Changes background",
      3
  ],
  [
      "What is the correct way to write a JavaScript array?",
      "var colors = 'red', 'green', 'blue';",
      "var colors = ['red', 'green', 'blue'];",
      "var colors = (1:'red', 2:'green');", "array = ['red','green','blue']",
      2
  ],
  [
      "Which HTML tag is used to define an internal style sheet?", "<style>",
      "<script>", "<css>", "<link>", 1
  ],
  [
      "Which property is used in CSS to make a flex container?",
      "display: grid;", "display: table;", "display: flex;",
      "display: block;", 3
  ],
  [
      "Which tag is used to link an external JavaScript file?",
      "<script src='...'>", "<js href='...'>", "<link rel='script'>",
      "<external-js>", 1
  ],
  [
      "What does HTML stand for?", "Hyper Trainer Marking Language",
      "Hyper Text Marketing Language", "Hyper Text Markup Language",
      "Hyper Tool Markup Language", 3
  ],
  [
      "Which HTTP method is used to request data from a specified resource?",
      "POST", "GET", "PUT", "FETCH", 2
  ],
  [
      "What does CSS stand for?", "Creative Style Sheets",
      "Cascading Style Sheets", "Computer Style Sheets",
      "Colorful Style Sheets", 2
  ],
  [
      "Which JavaScript method is used to select an element by ID?",
      "getElementsById()", "getElementById()", "querySelector()",
      "fetchById()", 2
  ],
  [
      "Which HTML tag is used to display a table?", "<tbl>", "<table>",
      "<tab>", "<tr>", 2
  ],
  [
      "Inside which HTML element do we put the JavaScript?", "<js>",
      "<script>", "<code>", "<javascript>", 2
  ],
  [
      "Which input type in HTML is used for selecting multiple options?",
      "text", "checkbox", "radio", "number", 2
  ],
  [
      "Which is not a valid HTML5 semantic element?", "<article>",
      "<section>", "<footer>", "<container>", 4
  ],
  [
      "Which CSS property is used to change the text color of an element?",
      "fgcolor", "color", "font-color", "text-color", 2
  ],
  [
      "What is the correct CSS syntax to change the font size?",
      "font-size: 14px;", "text-size: 14px;", "font: size 14px;",
      "fontsize = 14;", 1
  ],
  [
      "Which SQL statement is used to extract data from a database?", "OPEN",
      "GET", "SELECT", "READ", 3
  ],
  [
      "What is the purpose of the <meta> tag in HTML?",
      "To link external files", "To provide metadata", "To style content",
      "To run scripts", 2
  ],
  [
      "Which company developed JavaScript?", "Microsoft", "Mozilla",
      "Netscape", "Sun Microsystems", 3
  ],
  [
      "Which of the following is not a JavaScript framework?", "React",
      "Angular", "Vue", "Django", 4
  ],
  [
      "Which HTML attribute is used to define inline styles?", "styles",
      "font", "style", "css", 3
  ],
  [
      "What is Bootstrap?", "JavaScript library", "A version control tool",
      "A CSS framework", "Web server", 3
  ],
  [
      "How do you write a comment in JavaScript?", "// comment", "# comment",
      "<!-- comment -->", "/* comment */", 1
  ],
  [
      "What is the default position of an HTML element?", "absolute",
      "fixed", "relative", "static", 4
  ],
  [
      "Which HTML tag is used to make text italic?", "<italic>", "<em>",
      "<i>", "<it>", 3
  ]
]

levels = [
  1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
  1250000, 2500000, 5000000, 10000000, 20000000, 30000000, 40000000,
  50000000, 60000000, 70000000, 80000000, 90000000, 100000000, 200000000
]

money = 0
for i in range(0, len(questions)):
question = questions[i]
print(f"\n\nQuestion for Rs. {levels[i]}")
print(question[0])
print(f"a. {question[1]}          b. {question[2]}")
print(f"c. {question[3]}          d. {question[4]}")
reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
if reply == 0:
  money = levels[i - 1] if i > 0 else 0
  break
if reply == question[-1]:
  print(f"Correct answer, you have won Rs. {levels[i]}")
  if i == 4:
    money = 10000
  elif i == 9:
    money = 320000
  elif i == 14:
    money = 10000000
else:
  print("Wrong answer!")
  break

print(f"Your take home money is Rs. {money}")
