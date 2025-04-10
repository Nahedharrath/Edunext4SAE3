package com.esprit.microservice.microservice;


import com.esprit.microservice.microservice.Enum.CourseLevel;
import com.esprit.microservice.microservice.Enum.PackType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface CourseRepository extends JpaRepository<Course, Long> {
    Optional<Course> findCourseByCourseName(String courseName);
    List<Course> findByCourseNameContainingIgnoreCase(String courseName);
    List<Course> findByCategory_Id(Long categoryId);
    List<Course> findByCourseLevel(CourseLevel courseLevel);
    List<Course> findByPackType(PackType packType);
    List<Course> findTop5ByOrderByLikesDesc();

}
