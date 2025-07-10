import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.automobile import Automobile, Base

class TestAutomobileModel:
    """Testes para o modelo Automobile."""
    
    @pytest.fixture
    def db_session(self):
        """Fixture para criar uma sessão de banco de dados em memória."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
        session.close()
    
    def test_create_automobile(self, db_session):
        """Testa a criação de um automóvel."""
        automobile = Automobile(
            brand="Toyota",
            model="Corolla",
            year=2020,
            color="Branco",
            mileage=15000,
            price=85000.00,
            fuel_type="Flex",
            transmission="Automática",
            engine_size=1.8,
            num_doors=4,
            plate="ABC-1234"
        )
        
        db_session.add(automobile)
        db_session.commit()
        
        # Verificar se foi salvo corretamente
        saved_automobile = db_session.query(Automobile).filter_by(plate="ABC-1234").first()
        assert saved_automobile is not None
        assert saved_automobile.brand == "Toyota"
        assert saved_automobile.model == "Corolla"
        assert saved_automobile.year == 2020
        assert saved_automobile.price == 85000.00
    
    def test_automobile_repr(self):
        """Testa a representação string do automóvel."""
        automobile = Automobile(
            brand="Honda",
            model="Civic",
            year=2019
        )
        
        expected = "<Automobile(brand='Honda', model='Civic', year=2019)>"
        assert repr(automobile) == expected
    
    def test_unique_plate_constraint(self, db_session):
        """Testa a restrição de placa única."""
        automobile1 = Automobile(
            brand="Ford",
            model="Focus",
            year=2018,
            color="Azul",
            mileage=20000,
            price=65000.00,
            fuel_type="Gasolina",
            transmission="Manual",
            engine_size=2.0,
            num_doors=4,
            plate="XYZ-9876"
        )
        
        automobile2 = Automobile(
            brand="Chevrolet",
            model="Onix",
            year=2021,
            color="Prata",
            mileage=5000,
            price=55000.00,
            fuel_type="Flex",
            transmission="Manual",
            engine_size=1.0,
            num_doors=4,
            plate="XYZ-9876"  # Mesma placa
        )
        
        db_session.add(automobile1)
        db_session.commit()
        
        db_session.add(automobile2)
        
        # Deve gerar erro de integridade
        with pytest.raises(Exception):
            db_session.commit()
    
    def test_automobile_attributes(self):
        """Testa todos os atributos do automóvel."""
        automobile = Automobile(
            brand="Volkswagen",
            model="Golf",
            year=2022,
            color="Vermelho",
            mileage=8000,
            price=95000.00,
            fuel_type="Gasolina",
            transmission="Automática",
            engine_size=1.4,
            num_doors=4,
            plate="VWG-2022"
        )
        
        assert automobile.brand == "Volkswagen"
        assert automobile.model == "Golf"
        assert automobile.year == 2022
        assert automobile.color == "Vermelho"
        assert automobile.mileage == 8000
        assert automobile.price == 95000.00
        assert automobile.fuel_type == "Gasolina"
        assert automobile.transmission == "Automática"
        assert automobile.engine_size == 1.4
        assert automobile.num_doors == 4
        assert automobile.plate == "VWG-2022"

