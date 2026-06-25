from sqlalchemy import Column, BigInteger, Text, JSON, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from app.models.conversation import Conversation
from app.db.base import Base


class EmbeddingConversacion(Base):
    __tablename__ = "embeddings_conversaciones"

    id = Column(CHAR(36), primary_key=True)
    id_conversacion = Column(CHAR(36), ForeignKey("conversaciones.id_conversacion", ondelete="CASCADE"))
    embedding = Column(JSON, nullable=False)
    contenido = Column(Text, nullable=False)

    conversacion = relationship("Conversation", backref="embeddings")
