from chat import ask, build_index

qa = [

    {"q": "How old is the patient?", "expected": "70"},
    {"q": "Who does he live with?", "expected": "Wife"},
    {"q": "What medical history is noted for the patient?", "expected": "DM (Diabetes Mellitus)"},
    {"q": "When did the patient undergo a left total hip placement?", "expected": "3/1/16"},
    {"q": "Where was the patient transferred for rehab from 3/5-4/5/16?", "expected": "SNF (Skilled Nursing Facility)"},
    {"q": "When did PT and SN evaluate the patient to initiate care?", "expected": "4/7/16"},
    {"q": "How many PT and SN visits did the physician order?", "expected": "7 PT visits and 4 SN visits"},
    {"q": "What type of house does the patient live in?", "expected": "2-story house"},
    {"q": "What assistive device does the patient use to ambulate?", "expected": "FFW (Front Facing Walker)"},
    {"q": "How far can the patient currently ambulate with a walker?", "expected": "15 feet"},
    {"q": "Where exactly is the chronic DM ulcer located?", "expected": "Left medial metatarsal head"},
    {"q": "When is the patient's next Wound Care Clinic (WCC) visit?", "expected": "5/20/16"},
    {"q": "What is the patient's specific primary care physician's name?", "expected": "I don't know / Not mentioned in text"},
    {"q": "What brand of wheelchair does the patient use?", "expected": "I don't know / Not mentioned in text"},
    {"q": "What floor of the 2-story house is the patient's bedroom located on?", "expected": "I don't know / Not mentioned in text"},
    {
        "q": "Why is the patient considered homebound according to the clinical status?", 
        "expected": "Because he lives in a 2-story house and has an unsteady gait combined with stairs."
    },
    {
        "q": "Who is the primary informal/home caregiver that the PT and SN will be training?", 
        "expected": "The patient's wife."
    },
    {
        "q": "How many days did the patient spend in the Skilled Nursing Facility (SNF) for rehab?", 
        "expected": "31 days (from 3/5 to 4/5/16)."
    },
    {
        "q": "Which specific mobility task requires the highest level of physical assistance?", 
        "expected": "Sit to supine (maximum assist)."
    },
    {
        "q": "Based on the wound dressing schedule, what specific date will the wife perform her very first independent dressing change?", 
        "expected": "I don't know / Not mentioned in text" 
    }
]

collection = build_index("summary.pdf")

for i, pair in enumerate(qa, start=1):
    answer = ask(collection, pair["q"])
    print(f"\nQ{i}: {pair['q']}")
    print(f"Expected: {pair['expected']}")
    print(f"Got:      {answer}")
