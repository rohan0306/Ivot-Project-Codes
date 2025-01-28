totalregusers = $$response
totalreguserpilot = $$result
totalpilotaenglish = $$pilot_aenglish
totalpilotaspanish = $$pilot_aspanish
totalpilotcenglish = $$pilot_cenglish
totalpilotcspanish = $$pilot_cspanish
Activeusers = $$final
Perday = $$per_day
EntryCompletedStudents = $$retrieve_store_entry
BasicCompletedStudents = $$retrieve_store_basic
	

final_output = dict()

# Assign totalRegUsers from totalregusers
final_output["totalRegUsers"] = totalregusers[0]["totalRegUsers"]

# Add each campaign as a separate key from totalreguserpilot
for entry in totalreguserpilot:
    final_output[entry["_id"]] = entry["count"]

if totalpilotaenglish:
    final_output["PilotAEnglish"] = totalpilotaenglish[0]["PilotAEnglish"]
else:
    final_output["PilotAEnglish"] = 0

final_output["PilotASpanish"] = totalpilotaspanish[0]["PilotASpanish"]

final_output["PilotCEnglish"] = totalpilotcenglish[0]["PilotCEnglish"]

final_output["PilotCSpanish"] = totalpilotcspanish[0]["PilotCSpanish"]

final_output["activeStudentsCount"] = Activeusers[0]["activeStudentsCount"]

if Perday:  # Check if the list is not empty
    final_output["one_day_ago_count"] = Perday[0]["one_day_ago_count"]
else:
    final_output["one_day_ago_count"] = 0  # Set to 0 if no data for the day

#final_output["one_day_ago_count"] = Perday[0]["one_day_ago_count"] #last24hrs

final_output["entryCompletedStudents"] = EntryCompletedStudents[0]["entryCompletedStudents"]

if BasicCompletedStudents:
    final_output["basicCompletedStudents"] = BasicCompletedStudents[0]["basicCompletedStudents"]
else:
    final_output["basicCompletedStudents"] = 0

%%last%% = final_output
