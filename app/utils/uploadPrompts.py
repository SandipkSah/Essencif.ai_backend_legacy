from app.models.context import Context
from app.models.parameter import Parameter
from app.models.prompt import Prompt
from app.models import SolutionGroup  # Import SolutionGroup model


# async def insert_contexts(contexts):
#     print(contexts, "just to see what kind of contexts is being uploaded")
#     print("and the owner and its type are", contexts[0].get("owner"), type(contexts[0].get("owner")))
#     try:
#         inserted_count = 0
#         for context in contexts:
#             # Create a dictionary with the correct field names
#             context_data = {
#                 "owner": context.get("owner"),  # Foreign key reference
#                 "context_name": context.get("context_name", ""),
#                 "detailed_definition": context.get("detailed_definition", ""),
#                 "level": context.get("level", "n/a")
#             }

#             # Check if a context with the same name already exists for this owner
#             existing_context = await Context.filter(
#                 owner=context_data["owner"],
#                 context_name=context_data["context_name"]
#             ).first()

#             if not existing_context:
#                 await Context.create(**context_data)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading contexts: {e}")
#         raise

# async def insert_contexts(contexts):
#     print(contexts, "just to see what kind of contexts is being uploaded")
#     print("and the owner and its type are", contexts[0].get("owner"), type(contexts[0].get("owner")))
    
#     try:
#         inserted_count = 0
#         for context in contexts:
#             # Get the owner ID directly
#             owner_id = context.get("owner")
            
#             # Create a dictionary with the correct field names, passing owner_id directly
#             context_data = {
#                 "owner": owner_id,  # Pass the owner ID, not the object
#                 "context_name": context.get("context_name", ""),
#                 "detailed_definition": context.get("detailed_definition", ""),
#                 "level": context.get("level", "n/a")
#             }

#             # Check if a context with the same name already exists for this owner
#             existing_context = await Context.filter(
#                 owner=owner_id,
#                 context_name=context_data["context_name"]
#             ).first()

#             if not existing_context:
#                 await Context.create(**context_data)
#                 inserted_count += 1

#         return inserted_count

#     except Exception as e:
#         print(f"Error uploading contexts: {e}")
#         raise


async def insert_contexts(contexts):
    print(contexts, "just to see what kind of contexts is being uploaded")
    print("and the owner and its type are", contexts[0].get("owner"), type(contexts[0].get("owner")))
    
    try:
        inserted_count = 0
        for context in contexts:
            # Get the owner ID directly
            owner_id = context.get("owner")
            
            # Fetch the SolutionGroup object using the owner_id
            owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
            # Create a dictionary with the correct field names, passing owner object
            context_data = {
                "owner": owner,  # Now passing the SolutionGroup object, not the ID
                "context_name": context.get("context_name", ""),
                "detailed_definition": context.get("detailed_definition", ""),
                "level": context.get("level", "n/a")
            }

            # Check if a context with the same name already exists for this owner
            existing_context = await Context.filter(
                owner=owner,  # Compare with SolutionGroup object
                context_name=context_data["context_name"]
            ).first()

            if not existing_context:
                await Context.create(**context_data)
                inserted_count += 1

        return inserted_count

    except Exception as e:
        print(f"Error uploading contexts: {e}")
        raise


# async def insert_prompts(prompts):
#     print(prompts, "just to see what kind of prompt is being uploaded")
#     # print("and the owner and its type are", prompts[0].owner, type(prompts[0].owner))
#     try:
#         inserted_count = 0
#         for prompt in prompts:
#             # prompt = {k.lower(): v for k, v in prompt.items()}  # Normalize keys
            
#             # Create a dictionary with the correct field names
#             prompt_data = {
#                 "owner": prompt.get("owner"),  # Assuming owner is the ID of the SolutionGroup
#                 "prompt_name": prompt.get("prompt_name", ""),
#                 "detailed_definition": prompt.get("detailed_definition", ""),
#                 "level": prompt.get("level", "n/a")
#             }
            
#             # Check if prompt with the same name already exists for this owner
#             existing_prompt = await Prompt.filter(
#                 owner=prompt_data["owner"],
#                 prompt_name=prompt_data["prompt_name"]
#             ).first()
            
#             if not existing_prompt:
#                 await Prompt.create(**prompt_data)
#                 inserted_count += 1
            
#         return inserted_count
        
#     except Exception as e:
#         print(f"Error uploading prompts: {e}")
#         raise


async def insert_prompts(prompts):
    print(prompts, "just to see what kind of prompt is being uploaded")
    # print("and the owner and its type are", prompts[0].owner, type(prompts[0].owner))
    
    try:
        inserted_count = 0
        for prompt in prompts:
            # Get the owner ID directly
            owner_id = prompt.get("owner")
            
            # Fetch the SolutionGroup object using the owner_id
            owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
            # Create a dictionary with the correct field names, passing owner object
            prompt_data = {
                "owner": owner,  # Now passing the SolutionGroup object, not the ID
                "prompt_name": prompt.get("prompt_name", ""),
                "detailed_definition": prompt.get("detailed_definition", ""),
                "level": prompt.get("level", "n/a")
            }
            
            # Check if a prompt with the same name already exists for this owner
            existing_prompt = await Prompt.filter(
                owner=owner,  # Compare with SolutionGroup object
                prompt_name=prompt_data["prompt_name"]
            ).first()
            
            if not existing_prompt:
                await Prompt.create(**prompt_data)
                inserted_count += 1
        
        return inserted_count
        
    except Exception as e:
        print(f"Error uploading prompts: {e}")
        raise


# async def insert_parameters(parameters):
#     print(parameters, "just to see what kind of parameters is being uploaded")
#     # print("and the owner and its type are", parameters[0].owner, type(parameters[0].owner))
#     try:
#         inserted_count = 0
#         for parameter in parameters:
#             # Create a dictionary with the correct field names
#             parameter_data = {
#                 "owner": parameter.get("owner", ""),  # Foreign key reference
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
#                 owner=parameter_data["owner"],
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

# from .models import SolutionGroup  # Import SolutionGroup model

async def insert_parameters(parameters):
    print(parameters, "just to see what kind of parameters are being uploaded")
    # print("and the owner and its type are", parameters[0].owner, type(parameters[0].owner))
    
    try:
        inserted_count = 0
        for parameter in parameters:
            # Get the owner ID directly
            owner_id = parameter.get("owner")
            
            # Fetch the SolutionGroup object using the owner_id
            owner = await SolutionGroup.get(solution_group_id=owner_id)  # Fetch the SolutionGroup object
            
            # Create a dictionary with the correct field names, passing owner object
            parameter_data = {
                "owner": owner,  # Pass the SolutionGroup object, not the ID
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
                owner=owner,  # Compare with SolutionGroup object
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
