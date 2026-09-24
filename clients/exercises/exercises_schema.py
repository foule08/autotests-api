from pydantic import BaseModel, Field

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение упражнений
    """

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание стрктуры запроса для создания упражнения
    """

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроа для обновления упражнения
    """

    title: str | None
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str | None
    estimated_time: str = Field(alias="estimatedTime")


class ExerciseSchema(BaseModel):
    """
    Модель упражнения
    """

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа от сервера для создания упражнения
    """

    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа от сервера для получения упражнения
    """

    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа от сервера для получения упражнений
    """

    exercises: list[ExerciseSchema]


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа от сервера для обновления упражнения
    """

    exercise: ExerciseSchema