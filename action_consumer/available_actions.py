from action_consumer.available_actions_enum import Action


def get_available_actions(action_input,mouse_input):

    available_actions = {}
    for action in Action:
        if 'MOUSE' not in str(action).upper():
            available_actions.update({action: action_input.get(action)})

    for action in Action:
        if 'MOUSE' in str(action).upper():
            available_actions.update({action: mouse_input.get(action)})

    return available_actions
