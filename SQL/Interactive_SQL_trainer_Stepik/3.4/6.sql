SET @num_pr := 0;
SET @row_num := 1;
   
UPDATE applicant_order
    SET str_id = IF(program_id = @num_pr,
                    @row_num := @row_num + 1,
                    @row_num := 1 AND @num_pr := @num_pr + 1);