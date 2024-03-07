from django.contrib.auth.tokens import PassowrdResetTokenGenerator
from six import text_type

class TokenGenerator(PassowrdResetTokenGenerator): 
    def _make_hash_value(self, user, timestamp): 
        return (
            text_type(user.pk) + text_type(timestamp)
        )
generate_token = TokenGenerator()