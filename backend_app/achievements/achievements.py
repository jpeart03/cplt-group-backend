from django.utils import timezone
import datetime

def check_message_achievements(user, messages, this_recipient):
    new_unlocks = []
    personal_messages = [message for message in messages if message.recipient.relationship_type == 'Personal']
    professional_messages = [message for message in messages if message.recipient.relationship_type == 'Professional']
    recipient_messages = [message for message in messages if message.recipient == this_recipient]

    # Worlds Best Boss Levels
    
    if not user.worlds_best_boss_1 and len(professional_messages) >= 5:
        user.worlds_best_boss_1 = True
        new_unlocks.append("World's Best Boss - Level 1")

    if not user.worlds_best_boss_2 and len(professional_messages) >= 25:
        user.worlds_best_boss_2 = True
        new_unlocks.append("World's Best Boss - Level 2")
    
    if not user.worlds_best_boss_3 and len(professional_messages) >= 100:
        user.worlds_best_boss_3 = True
        new_unlocks.append("World's Best Boss - Level 3")


    # Cassanova Levels
    if not user.cassanova_1 and len(personal_messages) >= 5:
        user.cassanova_1 = True
        new_unlocks.append("Cassanova - Level 1")

    if not user.cassanova_2 and len(personal_messages) >= 25:
        user.cassanova_2 = True
        new_unlocks.append("Cassanova - Level 2")
    
    if not user.cassanova_3 and len(personal_messages) >= 100:
        user.cassanova_3 = True
        new_unlocks.append("Cassanova - Level 3")


    # It Takes Committment Levels
    message_weeks = [(message.send_date.strftime('%U'), message.send_date.strftime('%Y')) for message in messages]
    this_week = (timezone.now().date().strftime('%U'), timezone.now().date().strftime('%Y'))

    def check_weeks(week, year, num_week_lookback, message_weeks):
        week = int(week)
        year = int(year)
        start_week = week - num_week_lookback

        if start_week <= 0:
            start_week = start_week + 52
            start_year = int(year) - 1

            relevant_weeks = [(str(x), str(start_year)) for x in range(start_week, 53)]
            relevant_weeks.extend([(str(x), str(year))] for x in range(week))
        else:
            relevant_weeks = [(str(x), str(year)) for x in range(start_week, week)]

        return all(relevant_week in message_weeks for relevant_week in relevant_weeks)


    if not user.it_takes_committment_1 and check_weeks(this_week[0], this_week[1], 4, message_weeks):
        user.it_takes_committment_1 = True
        new_unlocks.append('It Takes Committment - Level 1')

    if not user.it_takes_committment_2 and check_weeks(this_week[0], this_week[1], 24, message_weeks):
        user.it_takes_committment_2 = True
        new_unlocks.append('It Takes Committment - Level 2')

    if not user.it_takes_committment_3 and check_weeks(this_week[0], this_week[1], 51, message_weeks):
        user.it_takes_committment_3 = True
        new_unlocks.append('It Takes Committment - Level 3')


    # Stand-alone Achievements
    message_contents = [message.content for message in messages]
    message_lengths = [len(content) for content in message_contents]

    if not user.short_and_sweet and (min(message_lengths) <= 10):
        user.short_and_sweet = True
        new_unlocks.append("Short and Sweet")

    if not user.dickens and (max(message_lengths) >= 200):
        user.dickens = True
        new_unlocks.append("Dickens")


    contains_smiley = [content for content in message_contents if ':)' in content]

    if not user.old_school and (len(contains_smiley) >= 1):
        user.old_school = True
        new_unlocks.append("Old School")


    latest_messages = [message.send_date for message in recipient_messages if message.send_date.date() < timezone.now().date()]
    latest_message = max(latest_messages)

    if not user.forget_me_not and (timezone.now() - latest_message) >= datetime.timedelta(days=14):
        user.forget_me_not = True
        new_unlocks.append("Forget Me Not")

    
    message_times = [message.send_date.strftime('%H') for message in messages]
    lunch_times = ['11', '12']
    sleep_times = ['00', '01', '02', '03', '04', '05']
    
    if not user.lunch_break and any(lunch_time in message_time for lunch_time in lunch_times for message_time in message_times):
        user.lunch_break = True
        new_unlocks.append('Lunch Break')

    if not user.sleep_mode and any(sleep_time in message_time for sleep_time in sleep_times for message_time in message_times):
        user.sleep_mode = True
        new_unlocks.append('I hope their phone was in sleep mode')


    user.save()
    return new_unlocks




def check_recipient_achievements(user, recipients):
    new_unlocks = []
    professional_recipients = [recipient for recipient in recipients if recipient.relationship_type == 'professional']

    # Networking Levels
    if not user.networking_1 and len(professional_recipients) >= 1:
        user.networking_1 = True
        new_unlocks.append("Networking - Level 1")

    if not user.networking_2 and len(professional_recipients) >= 10:
        user.networking_2 = True
        new_unlocks.append("Networking - Level 2")

    if not user.networking_3 and len(professional_recipients) >= 100:
        user.networking_3 = True
        new_unlocks.append("Networking - Level 3")


    # Stand-alone Achievements
    old_emails = ['@aol.com', '@yahoo.com', '@hotmail.com']
    emails = [recipient.email for recipient in recipients]
    has_old_email = any(old_email in email for old_email in old_emails for email in emails)

    if not user.what_year_is_it and has_old_email:
        user.what_year_is_it = True
        new_unlocks.append("What year is it?!?")


    user.save()
    return new_unlocks


    # sentimental = models.BooleanField(default=False)
    # send_i_mental = models.BooleanField(default=False)
    # nerd = models.BooleanField(default=False)
