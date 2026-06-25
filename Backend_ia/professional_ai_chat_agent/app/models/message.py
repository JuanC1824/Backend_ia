from sqlalchemy import Column, String, BigInteger, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base


class Message(Base):
    __tablename__ = "mensajes_ia"

    id_mensaje = Column(CHAR(36), primary_key=True, index=True)
    id_conversacion = Column(
        CHAR(36),
        ForeignKey("conversaciones.id_conversacion"),
        nullable=False
    )

    emisor = Column(Enum("usuario", "ia"), nullable=False)
    contenido = Column(Text, nullable=False)

    tokens_usados = Column(BigInteger, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    conversation = relationship("Conversation", back_populates="mensajes")
