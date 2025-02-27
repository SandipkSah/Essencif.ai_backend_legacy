from app.ormModels.context import Context
from app.ormModels.parameter import Parameter
from app.ormModels.prompt import Prompt


# async def insert_prompts(prompts, owner):
#     try:
#         inserted_count = 0
#         for prompt in prompts:
#             prompt = {k.lower(): v for k, v in prompt.items()}  # Normalize keys

#             if 'owner' not in prompt or not prompt['owner']:
#                 print(f"Skipping prompt due to missing owner: {prompt}")
#                 continue

#             existing_prompt = await Prompt.filter(
#                 owner=prompt['owner'],
#                 promptname=prompt['promptname']
#             ).first()

#             if not existing_prompt:
#                 await Prompt.create(**prompt)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading prompts: {e}")
#         raise
async def insert_prompts(prompts, owner):
    print(prompts, "just to see what kind of prompt is being uploaded")
    print("and the owner and its type are", owner, type(owner))
    try:
        inserted_count = 0
        for prompt in prompts:
            # prompt = {k.lower(): v for k, v in prompt.items()}  # Normalize keys
            
            # Create a dictionary with the correct field names
            prompt_data = {
                "owner_id": owner,  # Assuming owner is the ID of the UserGroup
                "name": prompt.get("name", ""),
                "detailed_definition": prompt.get("detailed_definition", ""),
                "level": prompt.get("level", "n/a")
            }
            
            # Check if prompt with the same name already exists for this owner
            existing_prompt = await Prompt.filter(
                owner_id=owner,
                name=prompt_data["name"]
            ).first()
            
            if not existing_prompt:
                await Prompt.create(**prompt_data)
                inserted_count += 1
            
        return inserted_count
        
    except Exception as e:
        print(f"Error uploading prompts: {e}")
        raise

async def insert_parameters(parameters, owner):
    print(parameters, "just to see what kind of parameters is being uploaded")
    print("and the owner and its type are", owner, type(owner))
    try:
        inserted_count = 0
        for parameter in parameters:
            # Create a dictionary with the correct field names
            parameter_data = {
                "owner_id": owner,  # Foreign key reference
                "parameter_set": parameter.get("parameter_set", ""),
                "engine": parameter.get("engine", ""),
                "max_tokens": parameter.get("max_tokens", 0),
                "temperature": parameter.get("temperature", 0.0),
                "top_p": parameter.get("top_p", 0.0),
                "n": parameter.get("n", 1),
                "stream": parameter.get("stream", False),
                "presence_penalty": parameter.get("presence_penalty", 0.0),
                "frequency_penalty": parameter.get("frequency_penalty", 0.0),
                "username": parameter.get("username", ""),
                "level": parameter.get("level", "n/a")
            }

            # Check if parameter with the same attributes already exists
            existing_parameter = await Parameter.filter(
                owner_id=owner,
                parameter_set=parameter_data["parameter_set"],
                engine=parameter_data["engine"],
                max_tokens=parameter_data["max_tokens"],
                temperature=parameter_data["temperature"],
                top_p=parameter_data["top_p"],
                n=parameter_data["n"],
                stream=parameter_data["stream"],
                presence_penalty=parameter_data["presence_penalty"],
                frequency_penalty=parameter_data["frequency_penalty"],
                username=parameter_data["username"]
            ).first()

            if not existing_parameter:
                await Parameter.create(**parameter_data)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading parameters: {e}")
        raise


async def insert_contexts(contexts, owner):
    print(contexts, "just to see what kind of contexts is being uploaded")
    print("and the owner and its type are", owner, type(owner))
    try:
        inserted_count = 0
        for context in contexts:
            # Create a dictionary with the correct field names
            context_data = {
                "owner_id": owner,  # Foreign key reference
                "name": context.get("name", ""),
                "detailed_definition": context.get("detailed_definition", ""),
                "level": context.get("level", "n/a")
            }

            # Check if a context with the same name already exists for this owner
            existing_context = await Context.filter(
                owner_id=owner,
                name=context_data["name"]
            ).first()

            if not existing_context:
                await Context.create(**context_data)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading contexts: {e}")
        raise


# async def insert_parameters(parameters, owner):
#     print(parameters, "just to see what kind of parameters is being uploaded")
#     print("and the owner and its type are", owner, type(owner))
#     try:
#         inserted_count = 0
#         for parameter in parameters:
#             parameter = {k.lower(): v for k, v in parameter.items()}  # Normalize keys

#             if 'owner' not in parameter or not parameter['owner']:
#                 print(f"Skipping parameter due to missing owner: {parameter}")
#                 continue

#             existing_parameter = await Parameter.filter(
#                 owner=parameter['owner'],
#                 parameterset=parameter['parameterset'],
#                 engine=parameter.get('engine'),
#                 max_tokens=parameter.get('max_tokens'),
#                 temperature=parameter.get('temperature'),
#                 top_p=parameter.get('top_p'),
#                 n=parameter.get('n'),
#                 stream=parameter.get('stream'),
#                 presence_penalty=parameter.get('presence_penalty'),
#                 frequency_penalty=parameter.get('frequency_penalty'),
#                 username=parameter.get('username')
#             ).first()

#             if not existing_parameter:
#                 await Parameter.create(**parameter)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading parameters: {e}")
#         raise


# async def insert_contexts(contexts,owner):
    print(contexts, "just to see what kind of contexts is being uploaded")
    print("and the owner and its type are", owner, type(owner))
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
