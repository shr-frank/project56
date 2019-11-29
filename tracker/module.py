def update_module(x,unique_squirrel_id):
    from django.apps import apps   
    sqs = Squirrel.objects.filter(unique_squirrel_id=unique_squirrel_id)
    model = apps.get_model('tracker', 'Squirrel')
    field_names = [f.name for f in model._meta.fields]
    for sq in sqs:
        for idx,f in field_names:
            if x[idx]:
                setattr(sq,f,x[idx])
        sq.save()
