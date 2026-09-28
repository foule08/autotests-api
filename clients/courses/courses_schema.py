from pydantic import BaseModel, Field, ConfigDict

from tools.fakers import fake

class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId", default=None)
    created_by_user_id: str = Field(alias="createdByUserId", default=None)


class GetCoursesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    maxScore: int
    minScore: int
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId", default=None)
    created_by_user_id: str = Field(alias="createdByUserId", default=None)

class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimatedTime: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory = fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema

class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema

class GetCourseResponseSchema(BaseModel):
    course: CourseSchema