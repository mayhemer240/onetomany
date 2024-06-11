from orm_base import Base
from db_connection import engine
from IntrospectionFactory import IntrospectionFactory
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint
from sqlalchemy import String, Integer, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from sqlalchemy import Table
from Department import Department
from constants import START_OVER, REUSE_NO_INTROSPECTION, INTROSPECT_TABLES
"""For consistency, the code below is implmented the same as Course"""

table_name: str = "sections"                 # The physical name of this table
# Find out whether the user is introspecting or starting over
introspection_type = IntrospectionFactory().introspection_type

if introspection_type == START_OVER or introspection_type == REUSE_NO_INTROSPECTION:
    
    class Section(Base):
        """
        A section represents a specific instance of a course offered during a semester.
        """
        
        __tablename__ = table_name

        departmentAbbreviation: Mapped[str] = mapped_column('department_abbreviation', String(10), primary_key=True)
        courseNumber: Mapped[int] = mapped_column('course_number', Integer, primary_key=True)
        sectionNumber: Mapped[int] = mapped_column('section_number', Integer, primary_key=True)
        semester: Mapped[str] = mapped_column('semester', String(10), nullable=False, primary_key=True)
        sectionYear: Mapped[int] = mapped_column('section_year', Integer, nullable=False, primary_key=True)
        building: Mapped[str] = mapped_column('building', String(6), nullable=False)
        room: Mapped[int] = mapped_column('room', Integer, nullable=False)
        schedule: Mapped[str] = mapped_column('schedule', String(6), nullable=False)
        startTime: Mapped[Time] = mapped_column('start_time', Time, nullable=False)

        instructor: Mapped[str] = mapped_column('instructor', String(80), nullable=False)

        __table_args__ = (
            UniqueConstraint("sectionYear", "semester", "schedule", "startTime", "building", "room",
                             name="sections_uk_01"),
            UniqueConstraint("sectionYear", "semester", "schedule", "startTime", "instructor",
                             name="sections_uk_02"),
            ForeignKeyConstraint(["departmentAbbreviation", "courseNumber"],
                                 ["courses.department_abbreviation", "courses.course_number"])
        )

        def __init__(self, departmentAbbreviation: str, courseNumber: int, sectionNumber: int,

                     semester: str, sectionYear: int, building: str, room: int,

                     schedule: str, startTime: Time, instructor: str):
            self.departmentAbbreviation = departmentAbbreviation
            self.courseNumber = courseNumber
            self.sectionNumber = sectionNumber
            self.semester = semester
            self.sectionYear = sectionYear
            self.building = building
            self.room = room
            self.schedule = schedule
            self.startTime = startTime
            self.instructor = instructor

        def __str__(self):
            return f"Section: {self.departmentAbbreviation} {self.courseNumber}-{self.sectionNumber}, " \
                   f"Semester: {self.semester} {self.sectionYear}, Location: {self.building} {self.room}, " \
                   f"Schedule: {self.schedule}, Start Time: {self.startTime}, Instructor: {self.instructor}"

elif introspection_type == INTROSPECT_TABLES:

    class Section(Base):
        __table__ = Table(table_name, Base.metadata, autoload_with=engine)
        departmentAbbreviation: Mapped[str] = column_property(__table__.c.department_abbreviation)
        courseNumber: Mapped[int] = column_property(__table__.c.course_number)
        sectionNumber: Mapped[int] = column_property(__table__.c.section_number)
        semester: Mapped[str] = column_property(__table__.c.semester)
        sectionYear: Mapped[int] = column_property(__table__.c.section_year)
        building: Mapped[str] = column_property(__table__.c.building)
        room: Mapped[int] = column_property(__table__.c.room)
        schedule: Mapped[str] = column_property(__table__.c.schedule)
        startTime: Mapped[Time] = column_property(__table__.c.start_time)
        instructor: Mapped[str] = column_property(__table__.c.instructor)

        def __init__(self, departmentAbbreviation: str, courseNumber: int, sectionNumber: int,
                 semester: str, sectionYear: int, building: str, room: int,
                 schedule: str, startTime: Time, instructor: str):
            self.departmentAbbreviation = departmentAbbreviation
            self.courseNumber = courseNumber
            self.sectionNumber = sectionNumber
            self.semester = semester
            self.sectionYear = sectionYear
            self.building = building
            self.room = room
            self.schedule = schedule
            self.startTime = startTime
            self.instructor = instructor
def set_section(session: Session, departmentAbbreviation: str, courseNumber: int, sectionNumber: int,
                   semester: str, sectionYear: int, building: str, room: int,
                   schedule: str, startTime: Time, instructor: str):
    """
    Create a new section in the database without enforcing uniqueness constraints.
    """
    section = Section(departmentAbbreviation=departmentAbbreviation, courseNumber=courseNumber,
                      sectionNumber=sectionNumber, semester=semester, sectionYear=sectionYear,
                      building=building, room=room, schedule=schedule, startTime=startTime,
                      instructor=instructor)
def __str__(self):
    return f"Section: {self.departmentAbbreviation} {self.courseNumber}-{self.sectionNumber}, " \
                   f"Semester: {self.semester} {self.sectionYear}, Location: {self.building} {self.room}, " \
                   f"Schedule: {self.schedule}, Start Time: {self.startTime}, Instructor: {self.instructor}"

"""Add the two instance methods to the class, regardless of whether we introspect or not."""
setattr(Section, 'set_section', set_section)
setattr(Course, '__str__', __str__) with section: from orm_base 

