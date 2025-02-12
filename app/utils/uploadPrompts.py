from app.ormModels.context import Context
from app.ormModels.parameter import Parameter
from app.ormModels.prompt import Prompt


async def insert_prompts(prompts):
    try:
        inserted_count = 0
        for prompt in prompts:
            prompt = {k.lower(): v for k, v in prompt.items()}  # Normalize keys

            if 'owner' not in prompt or not prompt['owner']:
                print(f"Skipping prompt due to missing owner: {prompt}")
                continue

            existing_prompt = await Prompt.filter(
                owner=prompt['owner'],
                promptname=prompt['promptname']
            ).first()

            if not existing_prompt:
                await Prompt.create(**prompt)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading prompts: {e}")
        raise


async def insert_parameters(parameters):
    try:
        inserted_count = 0
        for parameter in parameters:
            parameter = {k.lower(): v for k, v in parameter.items()}  # Normalize keys

            if 'owner' not in parameter or not parameter['owner']:
                print(f"Skipping parameter due to missing owner: {parameter}")
                continue

            existing_parameter = await Parameter.filter(
                owner=parameter['owner'],
                parameterset=parameter['parameterset'],
                engine=parameter.get('engine'),
                max_tokens=parameter.get('max_tokens'),
                temperature=parameter.get('temperature'),
                top_p=parameter.get('top_p'),
                n=parameter.get('n'),
                stream=parameter.get('stream'),
                presence_penalty=parameter.get('presence_penalty'),
                frequency_penalty=parameter.get('frequency_penalty'),
                username=parameter.get('username')
            ).first()

            if not existing_parameter:
                await Parameter.create(**parameter)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading parameters: {e}")
        raise


async def insert_contexts(contexts):
    try:
        inserted_count = 0
        for context in contexts:
            context = {k.lower(): v for k, v in context.items()}  # Normalize keys

            if 'owner' not in context or not context['owner']:
                print(f"Skipping context due to missing owner: {context}")
                continue

            existing_context = await Context.filter(
                owner=context['owner'],
                contextname=context['contextname']
            ).first()

            if not existing_context:
                await Context.create(**context)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading contexts: {e}")
        raise
