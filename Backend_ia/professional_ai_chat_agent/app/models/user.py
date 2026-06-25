from sqlalchemy import Column, String, Enum, Boolean
from sqlalchemy.dialects.mysql import CHAR
from app.db.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(CHAR(36), primary_key=True, index=True)

    correo = Column(String(255), nullable=False, unique=True)

    nombre_completo = Column(String(255), nullable=False)

    numero_documento = Column(String(255), nullable=True)

    tipo_documento = Column(String(255), nullable=True)

    password = Column(String(255), nullable=False)

    email_verificado = Column(Boolean, nullable=False, default=False)

    role = Column(
        Enum("ADMIN", "AGENTE", "CIUDADANO", name="role_enum"),
        nullable=True
    )
