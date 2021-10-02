def test():
    print("test")

def check_message_achievements(user, messages):
    new_unlocks = []
    personal_messages = [message for message in messages if message.recipient.relationship_type == 'personal']
    professional_messages = [message for message in messages if message.recipient.relationship_type == 'professional']
    # print("professional", professional_messages)
    # print('personal', personal_messages)

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


    # Stand-alone Achievements
    message_contents = [message.content for message in messages]
    message_lengths = [len(content) for content in message_contents]
    contains_smiley = [content for content in message_contents if ':)' in content]


    if not user.short_and_sweet and (min(message_lengths) <= 10):
        user.short_and_sweet = True
        new_unlocks.append("Short and Sweet")

    if not user.dickens and (max(message_lengths) >= 200):
        user.dickens = True
        new_unlocks.append("Dickens")

    if not user.old_school and (len(contains_smiley) >= 1):
        user.old_school = True
        new_unlocks.append("Old School")






    user.save()
    return new_unlocks




def check_recipient_achievements(user, recipients):
    new_unlocks = []
    # personal_recipients = [recipient for recipient in recipients if recipient.relationship_type == 'personal']
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


    # # Stand-alone Achievements
    # old_emails = ['@aol.com', '@yahoo.com', '@hotmail.com']
    # emails = [recipient.email for recipient in recipients]
    # has_old_email = any(old_email in emails for old_email in old_emails)


    user.save()
    return new_unlocks
  


    # sleep_mode = models.BooleanField(default=False)
    # lunch_break = models.BooleanField(default=False)
    # forget_me_not = models.BooleanField(default=False)


    # sentimental = models.BooleanField(default=False)
    # send_i_mental = models.BooleanField(default=False)
    # nerd = models.BooleanField(default=False)

    # what_year_is_it = models.BooleanField(default=False)




    # it_takes_committment_1 = models.BooleanField(default=False)
    # it_takes_committment_2 = models.BooleanField(default=False)
    # it_takes_committment_3 = models.BooleanField(default=False)