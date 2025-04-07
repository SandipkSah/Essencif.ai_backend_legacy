from app.models.context import Context
from app.models.parameter import Parameter
from app.models.prompt import Prompt
from app.models.solution_group import SolutionGroup  # Import SolutionGroup model


# async def insert_contexts(contexts, replace_prompt):
#     print(contexts, "just to see what kind of contexts is being uploaded")
#     print("and the owner and its type are", contexts[0].get("owner"), type(contexts[0].get("owner")))
    
#     try:
#         inserted_count = 0
#         for context in contexts:
#             # Get the owner ID directly
#             owner_id = context.get("owner")
            
#             # Fetch the SolutionGroup object using the owner_id
#             owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
#             # Create a dictionary with the correct field names, passing owner object
#             context_data = {
#                 "owner": owner,  # Now passing the SolutionGroup object, not the ID
#                 "context_name": context.get("context_name", ""),
#                 "detailed_definition": context.get("detailed_definition", ""),
#                 "level": context.get("level", "n/a")
#             }

#             # Check if a context with the same name already exists for this owner
#             existing_context = await Context.filter(
#                 owner=owner,  # Compare with SolutionGroup object
#                 context_name=context_data["context_name"]
#             ).first()

#             if not existing_context:
#                 await Context.create(**context_data)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading contexts: {e}")
#         raise

async def insert_contexts(contexts, replace_prompt=False):
    print(contexts, "just to see what kind of contexts is being uploaded")
    if contexts:
        print("and the owner and its type are", contexts[0].get("owner"), type(contexts[0].get("owner")))

    try:
        if not contexts:
            return 0

        inserted_count = 0

        # If replace_prompt is True, delete all existing contexts (ignoring owner)
        if replace_prompt:
            await Context.all().delete()

        for context in contexts:
            owner_id = context.get("owner")
            owner = await SolutionGroup.get(solution_group_id=owner_id)

            context_data = {
                "owner": owner,
                "context_name": context.get("context_name", ""),
                "detailed_definition": context.get("detailed_definition", ""),
                "level": context.get("level", "n/a")
            }

            if not replace_prompt:
                existing_context = await Context.filter(
                    owner=owner,
                    context_name=context_data["context_name"]
                ).first()

                if existing_context:
                    continue  # Skip duplicate

            await Context.create(**context_data)
            inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading contexts: {e}")
        raise


# async def insert_prompts(prompts, replace_prompt):
#     print(prompts, "just to see what kind of prompt is being uploaded")
#     # print("and the owner and its type are", prompts[0].owner, type(prompts[0].owner))
    
#     try:
#         inserted_count = 0
#         for prompt in prompts:
#             # Get the owner ID directly
#             owner_id = prompt.get("owner")
            
#             # Fetch the SolutionGroup object using the owner_id
#             owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
#             # Create a dictionary with the correct field names, passing owner object
#             prompt_data = {
#                 "owner": owner,  # Now passing the SolutionGroup object, not the ID
#                 "prompt_name": prompt.get("prompt_name", ""),
#                 "detailed_definition": prompt.get("detailed_definition", ""),
#                 "level": prompt.get("level", "n/a")
#             }
            
#             # Check if a prompt with the same name already exists for this owner
#             existing_prompt = await Prompt.filter(
#                 owner=owner,  # Compare with SolutionGroup object
#                 prompt_name=prompt_data["prompt_name"]
#             ).first()
            
#             if not existing_prompt:
#                 await Prompt.create(**prompt_data)
#                 inserted_count += 1
        
#         return inserted_count
        
#     except Exception as e:
#         print(f"Error uploading prompts: {e}")
#         raise

async def insert_prompts(prompts, replace_prompt=False):
    print(prompts, "just to see what kind of prompt is being uploaded")

    try:
        if not prompts:
            return 0

        inserted_count = 0

        # If replace_prompt is True, delete all existing prompts regardless of owner
        if replace_prompt:
            await Prompt.all().delete()

        for prompt in prompts:
            owner_id = prompt.get("owner")
            owner = await SolutionGroup.get(solution_group_id=owner_id)

            prompt_data = {
                "owner": owner,
                "prompt_name": prompt.get("prompt_name", ""),
                "detailed_definition": prompt.get("detailed_definition", ""),
                "level": prompt.get("level", "n/a")
            }

            if not replace_prompt:
                existing_prompt = await Prompt.filter(
                    owner=owner,
                    prompt_name=prompt_data["prompt_name"]
                ).first()

                if existing_prompt:
                    continue  # Skip duplicate

            await Prompt.create(**prompt_data)
            inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading prompts: {e}")
        raise


# async def insert_parameters(parameters, replace_prompt):
#     print(parameters, "just to see what kind of parameters are being uploaded")
#     # print("and the owner and its type are", parameters[0].owner, type(parameters[0].owner))
    
#     try:
#         inserted_count = 0
#         for parameter in parameters:
#             # Get the owner ID directly
#             owner_id = parameter.get("owner")
            
#             # Fetch the SolutionGroup object using the owner_id
#             owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
#             # Create a dictionary with the correct field names, passing owner object
#             parameter_data = {
#                 "owner": owner,  # Pass the SolutionGroup object, not the ID
#                 "parameter_set": parameter.get("parameter_set", ""),
#                 "engine": parameter.get("engine", ""),
#                 "max_tokens": parameter.get("max_tokens", 0),
#                 "temperature": parameter.get("temperature", 0.0),
#                 "top_p": parameter.get("top_p", 0.0),
#                 "n": parameter.get("n", 1),
#                 "stream": parameter.get("stream", False),
#                 "presence_penalty": parameter.get("presence_penalty", 0.0),
#                 "frequency_penalty": parameter.get("frequency_penalty", 0.0),
#                 "username": parameter.get("username", ""),
#                 "level": parameter.get("level", "n/a")
#             }

#             # Check if parameter with the same attributes already exists
#             existing_parameter = await Parameter.filter(
#                 owner=owner,  # Compare with SolutionGroup object
#                 parameter_set=parameter_data["parameter_set"],
#                 engine=parameter_data["engine"],
#                 max_tokens=parameter_data["max_tokens"],
#                 temperature=parameter_data["temperature"],
#                 top_p=parameter_data["top_p"],
#                 n=parameter_data["n"],
#                 stream=parameter_data["stream"],
#                 presence_penalty=parameter_data["presence_penalty"],
#                 frequency_penalty=parameter_data["frequency_penalty"],
#                 username=parameter_data["username"]
#             ).first()

#             if not existing_parameter:
#                 await Parameter.create(**parameter_data)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading parameters: {e}")
#         raise

async def insert_parameters(parameters, replace_prompt=False):
    print(parameters, "just to see what kind of parameters are being uploaded")

    try:
        if not parameters:
            return 0

        inserted_count = 0

        # If replace_prompt is True, delete all existing parameters regardless of owner
        if replace_prompt:
            await Parameter.all().delete()

        for parameter in parameters:
            owner_id = parameter.get("owner")
            owner = await SolutionGroup.get(solution_group_id=owner_id)

            parameter_data = {
                "owner": owner,
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

            if not replace_prompt:
                existing_parameter = await Parameter.filter(
                    owner=owner,
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

                if existing_parameter:
                    continue  # Skip duplicates

            await Parameter.create(**parameter_data)
            inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading parameters: {e}")
        raise
