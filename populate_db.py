from faker import Faker
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine, init_db
from src.models.automobile import Automobile
import random
from faker_vehicle import VehicleProvider

# Inicializa o banco de dados
init_db()

faker = Faker("pt_BR")
faker.add_provider(VehicleProvider)

def create_random_automobile():
    return Automobile(
        brand=faker.vehicle_make(),
        model=faker.vehicle_model(),
        year=random.randint(2000, 2024),
        color=faker.color_name(),
        mileage=random.randint(1000, 200000),
        price=round(random.uniform(15000.00, 200000.00), 2),
        fuel_type=random.choice(["Gasolina", "Etanol", "Diesel", "Flex", "Elétrico"]),
        transmission=random.choice(["Automática", "Manual"]),
        engine_size=round(random.uniform(1.0, 3.0), 1),
        num_doors=random.choice([2, 4]),
        plate=faker.license_plate()
    )

def populate_database(db: Session, num_automobiles: int = 100):
    print(f"Populando o banco de dados com {num_automobiles} automóveis...")
    for _ in range(num_automobiles):
        automobile = create_random_automobile()
        db.add(automobile)
    db.commit()
    print("Banco de dados populado com sucesso!")

if __name__ == "__main__":
    db = SessionLocal()
    populate_database(db)
    db.close()


