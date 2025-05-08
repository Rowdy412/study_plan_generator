import pandas as pd
import numpy as np
from datetime import timedelta

def generate_schedule(subjects, difficulties, exam_dates, total_hours_per_day):
    today = pd.to_datetime("today")
    
    difficulty_weights = {"Easy": 0.8, "Medium": 1.0, "Hard": 1.2}

   
    study_plan = {}

  
    remaining_subjects = {sub: {"difficulty": diff, "exam_date": pd.to_datetime(exam)} for sub, diff, exam in zip(subjects, difficulties, exam_dates)}

   
    current_day = today
    while remaining_subjects:
        
        remaining_subjects = {sub: details for sub, details in remaining_subjects.items() if details["exam_date"] > current_day}

        if not remaining_subjects:
            break  

        
        total_weight = sum(difficulty_weights[details["difficulty"]] for details in remaining_subjects.values())

       
        daily_schedule = {sub: round((total_hours_per_day * difficulty_weights[details["difficulty"]]) / total_weight, 2) 
                          for sub, details in remaining_subjects.items()}

     
        study_plan[current_day] = daily_schedule

       
        current_day += timedelta(days=1)

    
    study_df = pd.DataFrame.from_dict(study_plan, orient='index').reset_index()
    study_df.rename(columns={"index": "Day"}, inplace=True)
    
    return study_df
