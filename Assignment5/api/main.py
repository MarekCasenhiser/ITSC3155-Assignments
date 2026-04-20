from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)



@app.post("/recipe/", response_model=schemas.Order, tags=["recipe"])
def create_order(order: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe.create(db=db, recipe=recipe)


@app.get("/recipe/", response_model=list[schemas.Recipe], tags=["recipe"])
def read_recipe(db: Session = Depends(get_db)):
    return recipe.read_all(db)


@app.get("/recipe/{order_id}", response_model=schemas.Recipe, tags=["recipe"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipe.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipe/{recipe_id}", response_model=schemas.Recipe, tags=["recipe"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipe.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Recipe.update(db=db, recipe=recipe, recipe_id=recipe_id)


@app.delete("/recipe/{recipe_id}", tags=["recipe"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipe.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.delete(db=db, recipe_id=recipe_id)




@app.post("/sandwich/", response_model=schemas.Order, tags=["sandwich"])
def create_order(order: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwich.create(db=db, sandwich=sandwich)


@app.get("/sandwich/", response_model=list[schemas.Sandwich], tags=["sandwich"])
def read_sandwich(db: Session = Depends(get_db)):
    return sandwich.read_all(db)


@app.get("/sandwich/{order_id}", response_model=schemas.Sandwich, tags=["sandwich"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwich.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich


@app.put("/sandwich/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwich"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwich.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Sandwich.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)


@app.delete("/sandwich/{sandwich_id}", tags=["sandwich"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwich.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich.delete(db=db, sandwich_id=sandwich_id)




@app.post("/resource/", response_model=schemas.Order, tags=["resource"])
def create_order(order: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resource.create(db=db, resource=resource)


@app.get("/resource/", response_model=list[schemas.Resource], tags=["resource"])
def read_resource(db: Session = Depends(get_db)):
    return resource.read_all(db)


@app.get("/resource/{order_id}", response_model=schemas.Resource, tags=["resource"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resource.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resource/{resource_id}", response_model=schemas.Resource, tags=["resource"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resource.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Resource.update(db=db, resource=resource, resource_id=resource_id)


@app.delete("/resource/{resource_id}", tags=["resource"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resource.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.delete(db=db, resource_id=resource_id)




@app.post("/orderdetail/", response_model=schemas.OrderDetail, tags=["orderdetail"])
def create_orderdetail(orderdetail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return orderdetail.create(db=db, orderdetail=orderdetail)


@app.get("/orderdetail/", response_model=list[schemas.OrderDetail], tags=["orderdetail"])
def read_orderdetail(db: Session = Depends(get_db)):
    return orderdetail.read_all(db)


@app.get("/orderdetail/{orderdetail_id}", response_model=schemas.OrderDetail, tags=["orderdetail"])
def read_one_orderdetail(orderdetail_id: int, db: Session = Depends(get_db)):
    orderdetail = orderdetail.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orderdetail


@app.put("/orderdetail/{orderdetail_id}", response_model=schemas.OrderDetail, tags=["orderdetail"])
def update_one_orderdetail(orderdetail_id: int, orderdetail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    orderdetail_db = orderdetail.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Orderdetail.update(db=db, orderdetail=orderdetail, orderdetail_id=orderdetail_id)


@app.delete("/orderdetail/{orderdetail_id}", tags=["orderdetail"])
def delete_one_orderdetail(orderdetail_id: int, db: Session = Depends(get_db)):
    orderdetail = orderdetail.read_one(db, orderdetail_id=orderdetail_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orderdetail.delete(db=db, orderdetail_id=orderdetail_id)
