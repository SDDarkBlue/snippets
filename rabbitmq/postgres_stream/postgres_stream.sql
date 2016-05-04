CREATE OR REPLACE FUNCTION demo_trigger() RETURNS trigger AS
$demo_trigger$
   DECLARE
     message text := '{"undefined": True}';
     result record;
   BEGIN
     IF TG_OP = 'DELETE' THEN
         message := $message${$message$ ||
           $message$"operation": "delete", $message$ ||
           $message$"event_time": "$message$ || CURRENT_TIMESTAMP || $message$",$message$ ||
           $message$"data": { $message$ || 
           $message$"id": $message$ || OLD.id ||
           $message$ } }$message$;
     ELSIF TG_OP = 'UPDATE' THEN
         message := $message${$message$ ||
           $message$"operation": "update", $message$ ||
           $message$"event_time": "$message$ || CURRENT_TIMESTAMP || $message$",$message$ ||
           $message$"old": { $message$ || 
           $message$"id": $message$ || OLD.id || $message$,$message$ ||
           $message$"post_url": "$message$||OLD.post_url || $message$",$message$ ||
           $message$ },$message$ ||
           $message$"new": { $message$ || 
           $message$"id": $message$ || NEW.id || $message$,$message$ ||
           $message$"post_url": "$message$||NEW.post_url || $message$"$message$ ||
           $message$ } }$message$;    
     ELSIF TG_OP = 'INSERT' THEN
         message := $message${$message$ ||
           $message$"operation": "insert", $message$ ||
           $message$"event_time": "$message$ || CURRENT_TIMESTAMP || $message$",$message$ ||
           $message$"data": { $message$ || 
           $message$"id": $message$ || NEW.id || $message$,$message$ ||
           $message$"post_url": "$message$|| NEW.post_url || $message$",$message$ ||
           $message$"text": "$message$ || NEW.text|| $message$",$message$ ||
           $message$"html": "$message$ || NEW.html || $message$",$message$ ||
           $message$"thread_url": "$message$ || NEW.thread_url || $message$",$message$ ||
           $message$"timestamp": "$message$ || NEW.timestamp|| $message$",$message$ ||
           $message$"user_name": "$message$ || NEW.user_name|| $message$"$message$ ||
           $message$ } }$message$;    
     END IF;
     RAISE NOTICE 'Message: %', message;
     SELECT amqp.publish(1, 'nlp01', 'all', message) INTO result;
     RAISE NOTICE 'Result: %', result;
     RETURN NULL;
   END;
 $demo_trigger$ LANGUAGE plpgsql;

-- Add the trigger
CREATE TRIGGER stream_nlp_events
  AFTER INSERT OR UPDATE OR DELETE
  ON nlp_wjnhpost
  FOR EACH ROW
  EXECUTE PROCEDURE demo_trigger();
