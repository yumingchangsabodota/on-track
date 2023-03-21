from bson import ObjectId


def stringify_objid(field: str = "_id"):
    def inner(func):
        def wrapper(*args, **kwargs):
            results_dict = func(*args, **kwargs)
            results = []
            for result_dict in results_dict:
                if type(result_dict) == ObjectId:
                    result_dict = str(result_dict)
                elif field in result_dict and type(result_dict[field]) == ObjectId:
                    result_dict[field] = str(result_dict[field])
                results.append(result_dict)
            for r in results:
                if '_id' in r:
                    r['id'] = r['_id']
            return results
        return wrapper
    return inner


def objidify_str(field: str = "_id"):
    def inner(func):
        def wrapper(*args, **kwargs):
            result_dict = func(*args, **kwargs)
            if field in result_dict and type(result_dict[field]) == str:
                result_dict[field] = ObjectId(result_dict[field])
            return result_dict
        return wrapper
    return inner
