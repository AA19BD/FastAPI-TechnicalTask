from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.session import Base


class MyEnum(Enum):
    started = "started"
    ended = "ended"
    in_process = "in process"
    awaiting = "awaiting"
    canceled = "canceled"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    phone_number = Column(String(255), index=True, nullable=False)
    shopping_center_id = Column(
        Integer, ForeignKey("shopping_centers.id"), nullable=False
    )

    shopping_centers = relationship("ShoppingCenter", back_populates="employee")
    orders = relationship("Order", back_populates="employees")
    visits = relationship("Visit", back_populates="employees")


class ShoppingCenter(Base):
    __tablename__ = "shopping_centers"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    # employees_id = Column(Integer, ForeignKey("employees.id"))
    employee = relationship("Employee", back_populates="shopping_centers")
    customers = relationship("Customer", back_populates="shopping_centers")
    orders = relationship("Order", back_populates="shopping_centers")
    visits = relationship("Visit", back_populates="shopping_centers")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    phone_number = Column(String(255), index=True, nullable=False)
    shopping_center_id = Column(
        Integer, ForeignKey("shopping_centers.id"), nullable=False
    )

    shopping_centers = relationship("ShoppingCenter", back_populates="customers")
    orders = relationship("Order", back_populates="customers")
    visits = relationship("Visit", back_populates="customers")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    created_date = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    end_date = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    destination = Column(Integer, ForeignKey("shopping_centers.id"), nullable=False)
    author = Column(Integer, ForeignKey("customers.id"), nullable=False)
    status = Column(
        String(255),
        Enum("started", "ended", "in process", "awaiting", "canceled", name="MyEnum"),
        default="started",
        nullable=False,
    )
    executor = Column(Integer, ForeignKey("employees.id"), nullable=False)

    shopping_centers = relationship("ShoppingCenter", back_populates="orders")
    customers = relationship("Customer", back_populates="orders")
    employees = relationship("Employee", back_populates="orders")
    visits = relationship("Visit", back_populates="orders")


class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    created_date = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    executor = Column(Integer, ForeignKey("employees.id"), nullable=False)
    order = Column(Integer, ForeignKey("orders.id"), nullable=False)
    author = Column(Integer, ForeignKey("customers.id"), nullable=False)
    destination = Column(Integer, ForeignKey("shopping_centers.id"), nullable=False)

    employees = relationship("Employee", back_populates="visits")
    orders = relationship("Order", back_populates="visits")
    customers = relationship("Customer", back_populates="visits")
    shopping_centers = relationship("ShoppingCenter", back_populates="visits")
