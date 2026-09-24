from pydantic import BaseModel, Field, ConfigDict

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
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimatedTime: str

class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId", default=None)
    created_by_user_id: str = Field(alias="createdByUserId", default=None)

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema

class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema

class GetCourseResponseSchema(BaseModel):
    course: CourseSchema