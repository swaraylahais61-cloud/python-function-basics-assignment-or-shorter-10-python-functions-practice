#Tweet Character Limit Feature
def validate_tweet(input_text):
    if len(input_text) <= 140:
        return input_text
    return input_text[:140] + "..."


