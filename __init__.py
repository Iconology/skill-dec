from ovos_workshop.skills import OVOSSkill, intent_file_handler
import random

class DecisionMakerSkill(OVOSSkill):
    @intent_file_handler('sequential_decision.intent')
    def handle_sequential_decision_intent(self, message):
        # Extract the user's input
        user_input = message.data.get('user_input', '').lower()

        # Check if the user's input follows the expected pattern
        if 'or' in user_input:
            options = user_input.split('or')
            options = [option.strip() for option in options]

            if len(options) == 2:
                # Choose a random option
                chosen_option = random.choice(options)

                # Dynamically generate a spoken response based on the chosen option
                response = self.dialog_renderer.render('suggestion', {'chosen_option': chosen_option})

                # Speak the dynamically generated response
                self.speak(response)
                return

        # If the input doesn't match the expected pattern
        self.speak_dialog('invalid_input')

def create_skill():
    return DecisionMakerSkill()
